#!/usr/bin/env python3
"""Verify that dist/AGENTS.md is up to date.

This is a small wrapper around scripts/build-dist.py --check.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    build = str(ROOT / "scripts" / "build-dist.py")

    cmds = [
        [sys.executable, build, "--check"],
        [sys.executable, build, "--variant", "kernel", "--check"],
    ]

    for cmd in cmds:
        code = subprocess.call(cmd)
        if code != 0:
            raise SystemExit(code)


if __name__ == "__main__":
    main()
