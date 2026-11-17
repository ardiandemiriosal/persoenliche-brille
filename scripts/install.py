#!/usr/bin/env python3
"""Install one shared skill with a separate local profile configuration."""
import argparse
import json
from pathlib import Path


def install(home, repo, profile):
    profile = profile.resolve(strict=True)
    if not profile.is_file():
        raise ValueError('Profile must be a regular file')
    source = repo.resolve() / 'persoenliche-brille'
    destinations = [home / '.agents/skills/persoenliche-brille', home / '.claude/skills/persoenliche-brille']
    config = home / '.config/persoenliche-brille/config.json'
    for dest in destinations:
        if (dest.exists() or dest.is_symlink()) and dest.resolve() != source:
            raise FileExistsError(f'Refusing to overwrite {dest}')
    if config.exists() and json.loads(config.read_text()).get('profile_path') != str(profile):
        raise FileExistsError('Existing profile configuration differs; edit it deliberately')
    for dest in destinations:
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.is_symlink():
            dest.symlink_to(source, target_is_directory=True)
    config.parent.mkdir(parents=True, exist_ok=True)
    config.write_text(json.dumps({'profile_path': str(profile)}, ensure_ascii=False, indent=2) + '\n')
    config.chmod(0o600)
    print('Both skill links installed; profile config remains local.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', required=True, type=Path)
    args = parser.parse_args()
    install(Path.home(), Path(__file__).resolve().parents[1], args.profile)
