# Cloudflare setup

This is a static documentation site for **aibtc.io**, built with MkDocs Material. It uses the same document-site framework and monochrome dark styling as the AIBRC protocol site.

There is no platform backend in this repository. Serving the documentation requires no database, wallet, platform secrets or production-server access.

## 1. Upload to GitHub

Extract the source ZIP and upload its contents to the **root** of `aibtcbot/aibtcbot`.

Keep the existing `proofs/` directory. The ZIP carries the same two files already in that directory. The old wallet-signature README is preserved as `docs/wallet-signatures.md`; the root README now contains the platform's quick guide and documentation links.

Do not upload the ZIP itself or place all its files inside an extra parent folder.

## 2. Connect the repository to Cloudflare Workers

In **Workers & Pages**, create or select a Worker connected to this GitHub repository. Use:

| Setting | Value |
| --- | --- |
| Worker name | `aibtc-docs` |
| Production branch | `main` |
| Root directory | Repository root; leave blank or use `/` |
| Build command | `python3 -m pip install -r site/requirements.txt && python3 -m mkdocs build --strict -f site/mkdocs.yml` |
| Deploy command | `npx wrangler deploy` |
| Static asset directory | `site-build` — already declared in `wrangler.jsonc` |

The included `.python-version` pins Python 3.12.3, matching the local build used for this package. Cloudflare Workers Builds reads this version file. The build and deployment commands run from the repository root. Cloudflare handles its own GitHub connection and deployment authentication; do not put platform credentials in this repository.

This configuration uses **Workers Static Assets**. Do not configure the source directory `docs/` as the asset directory: the rendered HTML is generated in `site-build/`.

Official references: [Workers Builds configuration](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/) and [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/).

## 3. Attach aibtc.io

After the Worker preview is working, open the Worker and select **Settings → Domains & Routes → Add → Custom domain**. Enter:

```text
aibtc.io
```

The domain must be managed in the same Cloudflare account. If `aibtc.io` already has a DNS record, Worker route or redirect sending visitors to the trading platform, resolve that specific conflict when attaching the new documentation Worker. Keep `aibtc.bot` and the protocol domain `aibrc.io` unchanged.

Cloudflare provisions the custom-domain DNS record and certificate. `www.aibtc.io` is a separate hostname; add it or configure a redirect only if you want to use it.

Official reference: [Workers Custom Domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/).

## 4. Updating documentation

Edit the Markdown in this repository and commit to `main`. Cloudflare rebuilds the site from the same files shown on GitHub.

| Content | File |
| --- | --- |
| Quick guide / GitHub home | `README.md` |
| Six platform chapters | `docs/guide/` |
| API, MCP and npm | `docs/build-tools.md` |
| Support and official contacts | `docs/support.md` |
| Wallet signing notes | `docs/wallet-signatures.md` |
| Public code examples | `docs/code-examples.md` |
| Proof downloads | `proofs/` |
| Theme and navigation | `site/mkdocs.yml` and `site/assets/stylesheets/aibtc-dark.css` |

If the public proof script changes, update its checksum at the same time. This repository's script and the trading website's copy are independently versioned; a documentation update does not deploy the trading platform.

## Local build

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r site/requirements.txt
.venv/bin/python -m mkdocs build --strict -f site/mkdocs.yml
.venv/bin/python -m http.server 8000 --bind 127.0.0.1 --directory site-build
```

Open `http://127.0.0.1:8000/`. This serves only static documentation.
