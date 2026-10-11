#!/usr/bin/env python3
"""Validate released student starter notebooks (JSON and Python syntax only)."""
from __future__ import annotations
import ast
import json
import sys
from pathlib import Path

DEFAULT = Path('sessions/01_foundations/session01_persian_nlp_foundations.ipynb')
EXPECTED_MARKERS = {
    '01': ['Learning outcomes', 'UTF-8', 'Unicode', 'ZWNJ', 'Corpus audit',
           'Exit ticket', 'Final submission checklist'],
    '02': ['Learning outcomes', 'Regular Expressions', 'Information extraction',
           'normalize_spacing', 'preprocess_persian', 'Exit ticket',
           'Final submission checklist'],
}

def main(path: Path) -> int:
    errors = []
    try:
        notebook = json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        print(f'ERROR: cannot read notebook {path}: {exc}')
        return 1
    if notebook.get('nbformat') != 4:
        errors.append('Notebook must use nbformat 4.')
    cells = notebook.get('cells', [])
    if not cells:
        errors.append('Notebook has no cells.')
    markdown = '\n'.join(''.join(c.get('source', [])) for c in cells if c.get('cell_type') == 'markdown')
    meta = notebook.get('metadata', {}).get('language_processing_lab', {})
    session = str(meta.get('session', ''))
    if session not in EXPECTED_MARKERS:
        errors.append(f'Unknown/unreleased session metadata: {session}')
    if meta.get('student_starter') is not True:
        errors.append('student_starter metadata must be true.')
    for marker in EXPECTED_MARKERS.get(session, []):
        if marker not in markdown:
            errors.append(f'Missing expected section marker: {marker}')
    for index, cell in enumerate(cells):
        if cell.get('cell_type') != 'code':
            continue
        source = ''.join(cell.get('source', []))
        try:
            ast.parse(source)
        except SyntaxError as exc:
            errors.append(f'Code cell {index} has syntax error: {exc}')
    if errors:
        print(f'Notebook validation FAILED: {path}')
        for error in errors:
            print(' -', error)
        return 1
    print(f'Notebook validation passed: {path} ({len(cells)} cells)')
    return 0

if __name__ == '__main__':
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    raise SystemExit(main(target))
