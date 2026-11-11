"""Render the same Markdown on GitHub and the docs site; copy public downloads unchanged."""
import re
from pathlib import Path
from mkdocs.structure.files import File, Files

ROOT = Path(__file__).resolve().parent.parent

def on_files(files, config):
    paths = [ROOT / p for p in (
        'README.md', 'SOURCE_MAP.md', 'CLOUDFLARE.md', 'FAQ.md', 'llms.txt', 'llms-full.txt',
    )]
    for folder in ('docs', 'proofs', 'site/assets'):
        paths.extend(sorted((ROOT / folder).rglob('*')))
    # Keep Material/search assets supplied by MkDocs before adding repository sources.
    rendered = Files(f for f in files if f.src_uri.startswith(('assets/', 'search/')))
    for path in paths:
        if path.is_symlink():
            raise ValueError('Documentation source must not be a symlink')
        if path.is_file():
            rendered.append(File.generated(config, path.relative_to(ROOT).as_posix(), abs_src_path=str(path)))
    for path in sorted((ROOT / 'site/static').glob('*')):
        if path.is_symlink():
            raise ValueError('Static source must not be a symlink')
        if path.is_file():
            rendered.append(File.generated(config, path.name, abs_src_path=str(path)))
    return rendered


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != 'FAQ.md':
        return markdown
    # Preserve the FAQ's original text and numbering in the rendered headings.
    return '# ' + re.sub(
        r'(?<=\n\n)\d+\. [^\n]+(?=\n\n|$)',
        lambda match: ('### ' if match[0].endswith('?') else '## ') + match[0],
        markdown,
    )
