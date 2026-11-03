"""Render the same Markdown on GitHub and the docs site; copy public downloads unchanged."""
from pathlib import Path
from mkdocs.structure.files import File, Files

ROOT = Path(__file__).resolve().parent.parent

def on_files(files, config):
    paths = [ROOT / p for p in ('README.md', 'SOURCE_MAP.md', 'CLOUDFLARE.md')]
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
