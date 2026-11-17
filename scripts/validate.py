#!/usr/bin/env python3
"""Offline packaging/privacy checks; not a proof of skill effectiveness."""
from pathlib import Path
import importlib.util
import tempfile

root = Path(__file__).resolve().parents[1]
allowed = {'README.md', '.gitignore', 'persoenliche-brille/SKILL.md', 'persoenliche-brille/agents/openai.yaml', 'scripts/install.py', 'scripts/validate.py'}
for p in root.rglob('*'):
    if not p.is_file() or '.git' in p.relative_to(root).parts or '__pycache__' in p.parts:
        continue
    rel = p.relative_to(root).as_posix()
    assert rel in allowed, f'Unexpected public file: {rel}'
    content = p.read_text()
    assert '/' + 'Users/' not in content, f'Local path in {rel}'
    assert 'BEGIN ' + 'PRIVATE KEY' not in content, f'Key material in {rel}'
skill = (root / 'persoenliche-brille/SKILL.md').read_text()
assert skill.startswith('---\nname: persoenliche-brille\ndescription: ')
assert '\n---\n' in skill[4:]
spec = importlib.util.spec_from_file_location('brille_install', root / 'scripts/install.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
with tempfile.TemporaryDirectory() as tmp:
    home = Path(tmp)
    profile = home / 'private-profile.md'
    profile.write_text('synthetic fixture\n')
    module.install(home, root, profile)
    module.install(home, root, profile)
    a = home / '.agents/skills/persoenliche-brille'
    b = home / '.claude/skills/persoenliche-brille'
    assert a.resolve() == b.resolve() == root / 'persoenliche-brille'
    assert profile.read_text() == 'synthetic fixture\n'
    b.unlink()
    b.mkdir()
    try:
        module.install(home, root, profile)
    except FileExistsError:
        pass
    else:
        raise AssertionError('Conflicting install must be rejected')
print('PASS: package allowlist, local-path guard, shared installation, idempotence, collision protection')
