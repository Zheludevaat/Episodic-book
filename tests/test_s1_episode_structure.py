import pathlib
import re
import pytest

EPISODES = {
    'S0E00_Introduction_Prologue_Draft.md': None,
    'S1E01_Mallith_Episode_Draft.md': 'Receipt',
    'S1E02_Euphora7_Episode_Draft.md': 'No sharp edges',
    'S1E03_Lexis_Episode_Draft.md': 'For your safety',
    'S1E04_Equalia_Episode_Draft.md': 'No one above',
    'S1E05_Harmonia_Episode_Draft.md': 'Reframe that',
    'S1E06_Null13_Episode_Draft.md': 'Entropy is honest',
}

REQUIRED_SECTIONS = [
    '## Cold Open',
    '## Act I',
    '## Act II',
    '## Act III',
    '## Tag',
    '## Codex Minute',
]

PLACEHOLDER_PATTERNS = [r'TBD', r'TK', r'\?\?\?']

ROOT = pathlib.Path(__file__).resolve().parent.parent / 'episode_drafts'

@pytest.mark.parametrize('filename,expected_token', EPISODES.items())
def test_structure_and_token(filename, expected_token):
    content = (ROOT / filename).read_text(encoding='utf-8')
    for section in REQUIRED_SECTIONS:
        assert section in content, f"{filename} missing section: {section}"
    if expected_token:
        assert expected_token in content, f"{filename} missing token phrase"
    for pattern in PLACEHOLDER_PATTERNS:
        assert not re.search(pattern, content), f"{filename} contains placeholder {pattern}"
