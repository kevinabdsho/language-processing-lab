#!/usr/bin/env python3
"""Execute student starters from a clean kernel with notebook-relative paths."""
from pathlib import Path
from nbclient import NotebookClient
from nbformat import read

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    manifest = ROOT / 'RELEASED_SESSIONS.txt'
    allowed = [line.strip() for line in manifest.read_text(encoding='utf-8').splitlines()
               if line.strip() and not line.lstrip().startswith('#')]
    paths = []
    for folder in allowed:
        paths += sorted((ROOT / 'sessions' / folder).glob('*.ipynb'))
    if not paths:
        print('No notebooks found')
        return 1
    for path in paths:
        print('Executing', path.relative_to(ROOT), flush=True)
        nb = read(path, as_version=4)
        NotebookClient(nb, timeout=120, kernel_name='python3',
                       resources={'metadata': {'path': str(path.parent)}}).execute()
    print(f'{len(paths)} released student starters executed without exceptions')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
