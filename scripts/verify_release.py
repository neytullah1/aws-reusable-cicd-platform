#!/usr/bin/env python3
"""Fail-closed local guard; actual independent verification is NOT implemented."""
import sys
print('DENIED: external trusted provenance + authorization verifier is not configured.', file=sys.stderr)
sys.exit(1)
