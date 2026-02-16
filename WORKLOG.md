# WORKLOG

<!-- Dashboard cluster: first screenful — where are we, what's next, what's blocked -->

## Goal (from `SEED.md`)

Make the SEED Method publicly available and reusable by anyone on GitHub.

## Status

- Released v3.5 on 2026-02-14.
- Housekeeping complete: reduced always-loaded agent context and moved playbook
  skeleton templates into `docs/playbook/12-appendix-skeletons.md`.
- Housekeeping complete: split playbook sections into `docs/playbook/` and
  turned `SEED-Method.md` into a kernel + index.
- Housekeeping complete: added distribution builds:
  - `dist/AGENTS.md` (single-file bundle, generated)
  - `dist/AGENTS.kernel.md` (token-efficient kernel, generated)
- Housekeeping complete: added a skills.sh skill at `skills/seed/`
  (`SKILL.md` + `PLAYBOOK.md`, generated).
- Release v3.5.1 prepared, pending Owner sign-off.

## Next actions

1. Owner: sign off on v3.5.1 release.

## Open questions

- [question] Publish a patch release (v3.5.1) for the `AGENTS.md` kernel,
  appendix split, and modular playbook refactor? → RESOLVED (preparing release)

<!-- Detail cluster: reference material — how, why, what exactly -->

## Plan

(Next release scope TBD.)

## Tasks

(No active tasks.)

## Proof

See [README.md → Quick Start](README.md#quick-start)

### Environment notes

- No build steps, no dependencies — plain Markdown

### Last known result

- Date: 2026-02-16
- Result: PASS
- Notes: `check-dist.py` (both variants), `check-skill.py`, full markdown
  link/anchor/import integrity (27 files, 0 broken), SEED audit (§7) — all pass

## Decisions

- Generated dist and skill files committed to git — this project has no CI
  pipeline and consumers need the built artifacts (`dist/`, `skills/`) in the
  repo. Overrides default guardrail 7 ("No generated files in git").
  Freshness is enforced by `scripts/check-dist.py` and
  `scripts/check-skill.py`. [owner] 2026-02-16
- ASCII art logo style: gradient block Unicode — renders well across terminals
  and GitHub. [carry-over]
- License: CC BY 4.0 — permissive, appropriate for methodology/documentation.
  [carry-over]

## Lessons

- ASCII art rendering varies across platforms (terminal vs GitHub vs different
  fonts) — test in both before committing to a style; expect multiple
  iterations.
- Logo decision is purely subjective — only the Owner can decide. Don't iterate
  alone; checkpoint early on aesthetic choices.

## Practices

- Get Owner checkpoint on subjective/aesthetic choices early — prevents wasted
  iteration on preferences only the Owner can decide.
- Keep repo ceremony proportional to project size — a docs-only repo needs
  minimal proof (link checks, structure verification), not test frameworks.

## Working set

- Files touched:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `GEMINI.md`
  - `README.md`
  - `SEED-Method.md`
  - `dist/AGENTS.md`
  - `dist/AGENTS.kernel.md`
  - `docs/playbook/*.md`
  - `docs/playbook/12-appendix-skeletons.md`
  - `scripts/build-dist.py`
  - `scripts/check-dist.py`
  - `scripts/build-skill.py`
  - `scripts/check-skill.py`
  - `skills/seed/`
  - `SEED.md`
  - `SEED-Method-Cookbook.md`
  - `CHANGELOG.md`
  - `docs/releases/release-v3.5.1.md`

---

## Log

Entries through v3.5 archived to WORKLOG_ARCHIVE.md.

### 2026-02-16 — Publish as a skills.sh skill

Housekeeping only. No behavioral changes.

Changes:
- Added a skills.sh-compatible skill at `skills/seed/`:
  - `SKILL.md` (entrypoint)
  - `PLAYBOOK.md` (full playbook text)
- Added `scripts/build-skill.py` to generate the skill files from `dist/AGENTS.md`.
- Added `scripts/check-skill.py` to verify the skill file is up to date.
- Updated `README.md` with the install command and skill page link.

Proof:
- Manual: ran `./scripts/check-dist.py` and `./scripts/check-skill.py` (pass).

### 2026-02-16 — Add dist build and clean naming

Housekeeping only. No behavioral changes.

Changes:
- Added distribution builds for consumers:
  - `dist/AGENTS.kernel.md` (token-efficient kernel)
  - `dist/AGENTS.md` (single-file bundle)
- Added `scripts/build-dist.py` to generate both dist variants from canonical
  sources.
- Added `scripts/check-dist.py` to verify both dist variants are up to date.
- Removed legacy compact mirrors (`SEED-Method-compact*.md`).
- Moved appendix skeletons into `docs/playbook/12-appendix-skeletons.md`.
- Updated `README.md` Quick Start to recommend the kernel-first layout.

Proof:
- Manual: verified links resolve and files render correctly in Markdown.

### 2026-02-15 — Modularize playbook into section files

Housekeeping only. No behavioral changes.

Changes:
- Created `docs/playbook/` and moved §1–§11a content into section files.
- Rewrote `SEED-Method.md` to keep the always-on kernel plus an index and
  per-section stubs (to preserve existing anchors).
- Updated `AGENTS.md` pointers to reflect the new canonical structure.

Proof:
- Manual: verified links resolve and files render correctly in Markdown.

### 2026-02-15 — Compact always-loaded agent context

Housekeeping only. No behavioral changes.

Changes:
- Replaced root `AGENTS.md` with a compact, agent-agnostic kernel and pointers
  to canonical docs.
- Added `CLAUDE.md` and `GEMINI.md` shims that import `AGENTS.md`.
- Moved the playbook skeleton appendix out of `SEED-Method.md` into
  `docs/playbook/12-appendix-skeletons.md` and linked to it.

Proof:
- Manual: verified links resolve and files render correctly in Markdown.
