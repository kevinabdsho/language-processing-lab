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
    '03': ['Learning outcomes', 'Space-to-space', 'Word boundaries',
           'Byte Pair Encoding (BPE)', 'Evaluation', 'Exit ticket',
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
    if session == '03':
        data_dir = path.parent / 'data'
        gold_path = data_dir / 'tokenization_gold.tsv'
        train_path = data_dir / 'bpe_train.txt'
        try:
            gold_lines = [line for line in gold_path.read_text(encoding='utf-8').splitlines()
                          if line and not line.startswith('#')]
            assert len(gold_lines) >= 12, 'Need at least 12 gold evaluation examples.'
            records = [line.split('\t') for line in gold_lines]
            assert all(len(rec) == 3 and all(rec) for rec in records), 'Expected three nonempty TSV columns.'
            assert len({rec[0] for rec in records}) == len(records), 'Duplicate gold IDs.'
            assert all(rec[2].split('|') and all(rec[2].split('|')) for rec in records), 'Empty gold token.'
            for sample_id, text, annotation in records:
                cursor = 0
                for token in annotation.split('|'):
                    start = text.find(token, cursor)
                    assert start >= 0, f'Missing reference token for {sample_id}: {token!r}'
                    assert text[cursor:start].isspace() or start == cursor, f'Non-space gap in {sample_id}.'
                    cursor = start + len(token)
                assert not text[cursor:].strip(), f'Uncovered text in {sample_id}.'
            train_lines = [line for line in train_path.read_text(encoding='utf-8').splitlines() if line.strip()]
            assert len(train_lines) >= 12, 'Need at least 12 BPE training lines.'
            assert not ({rec[1] for rec in records} & set(train_lines)), 'Gold text leaked into training.'
        except (OSError, UnicodeError, AssertionError) as exc:
            errors.append(f'Session 03 data validation failed: {exc}')
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
