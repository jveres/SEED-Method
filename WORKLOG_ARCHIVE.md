# WORKLOG ARCHIVE

## Releases

| Release | Date       | Record                                                           |
| ------- | ---------- | ---------------------------------------------------------------- |
| v3.5.1  | 2026-02-16 | [docs/releases/release-v3.5.1.md](docs/releases/release-v3.5.1.md) |
| v3.5    | 2026-02-14 | [docs/releases/release-v3.5.md](docs/releases/release-v3.5.md)     |

---

## Archived lessons

(None yet.)

## Archived practices

(None yet.)

---

## Release v3.5.1 (2026-02-16)

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

---

## Release v3.5 (2026-02-14)

### 2026-02-14 — Final polish + audit (builder / Claude)

**Summary**

Final polish pass: ran SEED Method audit (§7), verified all internal links, checked guardrail compliance, populated Lessons and Practices, freshened WORKLOG snapshot sections. All tasks complete except release.

**Changes**

- Freshened `WORKLOG.md` — updated working set (was stale), added lessons and practices, updated proof result, marked Task 8 done
- Verified all 4 internal README links resolve correctly
- Verified repo structure matches README description
- No formatting or consistency issues found in deliverable files

**Proof run**

- Manual link verification: all internal links in README resolve (SEED-Method.md, SEED-Method-Cookbook.md, CHANGELOG.md, LICENSE)
- Repo structure: matches "What's in this repo" table exactly
- Audit: PASS on all phases, all 10 guardrails, all 5 state clarity checks

**Next**

1. Owner sign-off for release v3.5

#polish #audit #worklog

### 2026-02-14 — Owner checkpoint (builder / Claude)

**Summary**

Owner reviewed README and repo structure. Decided on logo variant E (rounded + asymmetric D), CC BY 4.0 license, and minimal GitHub files (LICENSE only, no .github templates). Added LICENSE file.

**Changes**

- Added `LICENSE` (CC BY 4.0)
- Updated `README.md` — added LICENSE to "What's in this repo" table
- Applied logo variant E after Owner selection

**Proof run**

- Manual inspection: LICENSE present, README table updated, logo renders correctly

**Feedback from jveres**

- Logo: variant E (rounded + asymmetric D) — approved
- License: CC BY 4.0 — approved
- GitHub files: keep minimal, no .github templates — approved

**Next**

1. Final polish pass
2. Prepare release for Owner sign-off

#checkpoint #license #logo

### 2026-02-14 — Bootstrap (builder / Claude)

**Summary**

Project bootstrapped for public GitHub release. Created SEED.md from Owner input, initialized git, wrote README.md with ASCII art logo and quick-start guide, created .gitignore and WORKLOG.md with plan/tasks.

**Changes**

- Created `SEED.md` — vision, constraints, guardrails, non-goals
- Initialized git repo on `main`
- Created `README.md` — ASCII logo, what/why/how, quick-start (copy + tell agent), artifact table, flow diagram, cookbook pointer, license
- Created `.gitignore` — secrets + .DS_Store
- Created `WORKLOG.md` — full dashboard + plan/tasks

**Proof run**

- Manual inspection: all files present, internal links consistent, README renders correctly in Markdown
- No automated proof (documentation-only repo)

**Next**

1. Owner checkpoint: review README and repo structure
2. Confirm license choice (CC BY 4.0)
3. Decide on GitHub-specific files (LICENSE, .github templates)

#bootstrap #readme #seed
