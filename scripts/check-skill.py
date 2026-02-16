#!/usr/bin/env python3
"""Verify that the skills/seed/ generated files are up to date.

This is a small wrapper around scripts/build-skill.py --check.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    cmd = [sys.executable, str(ROOT / "scripts" / "build-skill.py"), "--check"]
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
