#!/usr/bin/env python3
"""Structural validation only; NOT cryptographic verification or authorization."""
import json, re, sys
from pathlib import Path
SHA = re.compile(r'^[a-f0-9]{40}$')
DIGEST = re.compile(r'^sha256:[a-f0-9]{64}$')
REPO = re.compile(r'^[0-9]{12}\.dkr\.ecr\.[a-z0-9-]+\.amazonaws\.com/[a-z0-9._/-]+$')
def validate(doc):
    if doc.get('schema_version') != 1: raise ValueError('invalid schema_version')
    if doc.get('runtime') not in ('eks','ecs','lambda'): raise ValueError('invalid runtime')
    if doc.get('environment') not in ('dev','stage','prod'): raise ValueError('invalid environment')
    if not re.fullmatch(r'[a-z][a-z0-9-]{1,62}',doc.get('application','')): raise ValueError('invalid application')
    if not SHA.fullmatch(doc.get('git_sha','')): raise ValueError('invalid git_sha')
    art=doc.get('artifact',{})
    if not DIGEST.fullmatch(art.get('digest','')): raise ValueError('invalid artifact digest')
    if not REPO.fullmatch(art.get('repository','')): raise ValueError('invalid repository')
    if doc.get('approvals',{}).get('required') is not True: raise ValueError('approval requirement missing')
    return True
if __name__ == '__main__':
    try:
        validate(json.loads(Path(sys.argv[1]).read_text()))
        print('Structure valid. NOT authorized for deployment.')
    except (ValueError, KeyError, IndexError, OSError, json.JSONDecodeError) as exc:
        print(f'Invalid: {exc}',file=sys.stderr);sys.exit(1)
