#!/usr/bin/env python3
"""Checks members/*.md have name: and role:, and that no conflict markers were committed."""
import re
import subprocess
import sys
from pathlib import Path

errors = []
for f in sorted(Path("members").glob("*.md")):
    if f.name in ("README.md", "_template.md"):
        continue
    fields = {}
    for line in f.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*([A-Za-z_]+)\s*:\s*(.*?)\s*$", line)
        if m:
            fields[m.group(1).lower()] = m.group(2)
    for key in ("name", "role"):
        if not fields.get(key):
            errors.append((str(f), f"missing '{key}:' line"))
    print(f"  checked {f}: name={fields.get('name', '-')!r} role={fields.get('role', '-')!r}")

grep = subprocess.run(["git", "grep", "-n", "-I", "-E", r"^(<<<<<<<|>>>>>>>)( |$)|^=======$", "--", ".", ":(exclude).github"],
                      capture_output=True, text=True)
for line in grep.stdout.splitlines()[:10]:
    path, num, _ = line.split(":", 2)
    errors.append((path, f"conflict marker left at line {num}"))

if errors:
    for path, msg in errors:
        print(f"::error file={path}::{msg}")
    print(f"\nvalidate FAILED: {len(errors)} problem(s).")
    sys.exit(1)
print("\nvalidate passed.")
