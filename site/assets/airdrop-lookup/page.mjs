import { createLookup } from './lookup.mjs';

const form = document.querySelector('#airdrop-lookup');
const address = document.querySelector('#airdrop-address');
const result = document.querySelector('#airdrop-result');
let revision = 0;

const lookup = createLookup(async (token, prefix) => {
  const url = new URL('./shards/' + token + '/' + prefix + '.json', import.meta.url);
  const response = await fetch(url, { mode: 'same-origin', redirect: 'error' });
  if (!response.ok) throw new Error('Could not load shard');
  return response.json();
});

function show(state, matches = {}) {
  const templateId = state === 'empty' ? 'invalid' : state;
  const template = document.querySelector('#airdrop-' + templateId);
  const content = template.content.cloneNode(true);
  if (state === 'found') {
    for (const row of content.querySelectorAll('[data-token]')) {
      if (!matches[row.dataset.token]) row.remove();
    }
  }
  address.setAttribute('aria-invalid', String(state === 'invalid' || state === 'empty'));
  result.setAttribute('aria-busy', String(state === 'loading'));
  result.replaceChildren(content);
  result.dataset.state = state;
}

form.addEventListener('submit', async event => {
  event.preventDefault();
  const current = ++revision;
  const value = address.value;
  show('loading');
  try {
    const matches = await lookup(value);
    if (revision === current) show(matches.state, matches);
  } catch {
    if (revision === current) show('load-error');
  }
});

address.addEventListener('input', () => {
  revision++;
  address.removeAttribute('aria-invalid');
  result.setAttribute('aria-busy', 'false');
  result.replaceChildren();
  delete result.dataset.state;
});
