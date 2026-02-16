#!/usr/bin/env python3
"""Build (or verify) the single-file distribution playbook.

Outputs:
- dist/AGENTS.md: single-file playbook intended to be copied into a consuming
  repository as AGENTS.md.
- dist/AGENTS.kernel.md: token-efficient kernel intended to be copied into a
  consuming repository as AGENTS.md, together with docs/playbook/.

Canonical sources live in:
- SEED-Method.md (kernel + index)
- docs/playbook/*.md (sections)

This script intentionally removes the modular index/stubs and embeds full
section bodies.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

KERNEL_PATH = ROOT / "SEED-Method.md"
SECTION_DIR = ROOT / "docs" / "playbook"
DEFAULT_OUT_PATH = ROOT / "dist" / "AGENTS.md"
DEFAULT_KERNEL_OUT_PATH = ROOT / "dist" / "AGENTS.kernel.md"

SECTION_FILES = [
    "01-autonomy-contract.md",
    "02-bootstrap.md",
    "03-build.md",
    "04-prove.md",
    "05-worklog.md",
    "06-adapt.md",
    "07-audit.md",
    "08-seed-questions.md",
    "09-multi-agent.md",
    "10-release.md",
    "11-guardrails.md",
    "12-appendix-skeletons.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _rewrite_intro_for_consumers(text: str, *, variant: str) -> str:
    source_intro = (
        "This playbook is typically stored as `AGENTS.md` in a consuming repo\n"
        "(repo root). In this source repo, the canonical text is split across\n"
        "`SEED-Method.md` (kernel + index) and `docs/playbook/` (sections + appendix).\n"
    )

    if variant == "full":
        replacement = (
            "This playbook is stored as `AGENTS.md` in the repo root and is the "
            "canonical source of truth for agent behavior.\n"
        )
    elif variant == "kernel":
        replacement = (
            "This playbook is stored as `AGENTS.md` in the repo root.\n\n"
            "This file is the **kernel** (token-efficient). Load the relevant "
            "section(s) from `docs/playbook/` on demand.\n"
            "If the modular files are not present, use the single-file bundle "
            "or install the SEED skill (`jveres/The-SEED-Method@seed`).\n"
        )
    else:
        raise SystemExit(f"Unknown variant: {variant!r}")

    return text.replace(source_intro, replacement)


def build_dist_text() -> str:
    kernel = read_text(KERNEL_PATH)

    marker = "## Full playbook sections (modular)"
    if marker not in kernel:
        raise SystemExit(f"Marker not found in {KERNEL_PATH}: {marker!r}")

    kernel = kernel.split(marker, 1)[0].rstrip() + "\n\n"
    kernel = _rewrite_intro_for_consumers(kernel, variant="full")

    parts: list[str] = []

    # Keep the distribution file clean for copy/paste. Use a short HTML comment
    # that does not render in Markdown.
    parts.append(
        "<!-- Generated file: dist/AGENTS.md. Source: SEED-Method.md + "
        "docs/playbook/*.md -->\n\n"
    )
    parts.append(kernel)

    for name in SECTION_FILES:
        path = SECTION_DIR / name
        if not path.exists():
            raise SystemExit(f"Missing section source: {path}")

        text = read_text(path).rstrip() + "\n"

        # In the modular sources, 11-guardrails ends with a pointer to the
        # appendix. In the distribution build we embed the appendix, so drop the
        # pointer.
        if name == "11-guardrails.md":
            appendix_marker = "# Appendix — Skeletons"
            if appendix_marker in text:
                text = text.split(appendix_marker, 1)[0].rstrip() + "\n"

        parts.append("\n\n" + text)

    return "".join(parts).strip() + "\n"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--variant",
        choices=["full", "kernel"],
        default="full",
        help="Build variant (default: full)",
    )
    p.add_argument(
        "--out",
        default=None,
        help=(
            "Output path (default depends on --variant: "
            "full -> dist/AGENTS.md, kernel -> dist/AGENTS.kernel.md)"
        ),
    )
    p.add_argument(
        "--check",
        action="store_true",
        help="Check that the output is up to date; do not write",
    )
    return p.parse_args()


def _default_out_path(variant: str) -> Path:
    if variant == "full":
        return DEFAULT_OUT_PATH
    if variant == "kernel":
        return DEFAULT_KERNEL_OUT_PATH
    raise SystemExit(f"Unknown variant: {variant!r}")


def build_kernel_text() -> str:
    """Build the token-efficient kernel (kernel + modular index only).

    Note: the index uses plain file paths (not Markdown links) so the file can
    be copied from dist/ to a consuming repo root without breaking references.
    """

    text = read_text(KERNEL_PATH)

    marker = "## Full playbook sections (modular)"
    if marker not in text:
        raise SystemExit(f"Marker not found in {KERNEL_PATH}: {marker!r}")

    kernel = text.split(marker, 1)[0].strip() + "\n\n"
    kernel = _rewrite_intro_for_consumers(kernel, variant="kernel")

    index = """## Full playbook sections (modular)

Read only the section(s) you need for the current task.

- §1: `docs/playbook/01-autonomy-contract.md`
- §2: `docs/playbook/02-bootstrap.md`
- §3: `docs/playbook/03-build.md`
- §4: `docs/playbook/04-prove.md`
- §5–§5b: `docs/playbook/05-worklog.md`
- §6: `docs/playbook/06-adapt.md`
- §7: `docs/playbook/07-audit.md`
- §8: `docs/playbook/08-seed-questions.md`
- §9: `docs/playbook/09-multi-agent.md`
- §10–§10a: `docs/playbook/10-release.md`
- §11–§11a: `docs/playbook/11-guardrails.md`
- Appendix templates: `docs/playbook/12-appendix-skeletons.md`

"""

    # Add a short build header (does not render in Markdown).
    header = (
        "<!-- Generated file: dist/AGENTS.kernel.md. Source: SEED-Method.md + "
        "docs/playbook/*.md -->\n\n"
    )

    return (header + kernel + index).strip() + "\n"


def main() -> None:
    args = parse_args()

    out_path = Path(args.out) if args.out else _default_out_path(args.variant)

    if args.variant == "full":
        expected = build_dist_text()
    elif args.variant == "kernel":
        expected = build_kernel_text()
    else:
        raise SystemExit(f"Unknown variant: {args.variant!r}")

    if args.check:
        if not out_path.exists():
            print(f"Missing {out_path}. Run: ./scripts/build-dist.py")
            sys.exit(1)

        actual = out_path.read_text(encoding="utf-8")
        if actual != expected:
            print(f"Out of date: {out_path}. Run: ./scripts/build-dist.py")
            sys.exit(1)

        print(f"OK: {out_path} is up to date")
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(expected, encoding="utf-8")
    print(f"Wrote {out_path.relative_to(ROOT)} ({out_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
