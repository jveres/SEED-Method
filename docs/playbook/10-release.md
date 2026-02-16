## 10) Definition of Release Done (DoRD)

Use this checklist before declaring "done" / requesting Owner sign-off.

- [ ] **Vision delivered:** implementation matches `SEED.md` Vision and respects Constraints/Non-goals.
- [ ] **Tasks closed:** all planned tasks are completed, explicitly deferred, or explicitly dropped with reason.
- [ ] **Final proof passed:** required automated/manual proof executed for the full product; results recorded.
- [ ] **Guardrails clean:** no violations of default (§11) or project-specific guardrails.
- [ ] **No critical unknowns:** open questions are accepted by Owner or tracked as post-release items.
- [ ] **Learning captured:** `## Lessons` and `## Practices` are current; no unrecorded insights from the release.
- [ ] **Artifacts fresh:**
  - [ ] `WORKLOG.md` is final and fresh
  - [ ] `SEED.md` clarifications/process knobs/guardrails are up to date
- [ ] **README current:** run/prove instructions and known limitations match shipped behavior.
- [ ] **Working tree clean enough to hand over:** no ambiguous partial edits; rollback path is clear.
- [ ] **Owner sign-off requested:** explicit "ready for release" handoff sent.
- [ ] **(Optional) Release metadata:** version/tag/changelog created if repo workflow uses releases.

### Release readiness summary (optional, pre-sign-off)

```md
Release readiness: PASS
Date: YYYY-MM-DD
Scope: <what is included>
Proof summary: <commands/checklist + outcome>
Guardrail check: PASS / <list violations>
Deferred items: <none or list>
Owner sign-off: <requested/received>
```

After Owner sign-off, proceed to §10a.

---


## 10a) Post-release closeout (seal + reset)

After the Owner signs off on a release, perform closeout in two steps. The goal is to seal the completed release as an immutable record, then reset the working surface so the next release can start cleanly without losing auditability.

In multi-agent mode, the coordinator performs both steps. Contributing agents do not modify `WORKLOG.md`, create release records, or perform archive/reset directly.

### Release ID scheme

Default: **SemVer** (`vX.Y.Z`). If the project uses a different scheme (date-based, incremental, etc.), record the convention in `SEED.md` → `### Process knobs`.

### Step A — Seal (create the release marker)

1. **Tag the commit** (preferred): `vX.Y.Z` on the exact release commit.
2. **Create the release record:** `docs/releases/release-vX.Y.Z.md`

The release record is the canonical, self-contained artifact for this release. It must include:

```md
# Release vX.Y.Z

- **Date:** YYYY-MM-DD
- **Tag / commit:** <tag or hash>

## Scope

- Included:
- Excluded / deferred:

## Proof summary

(Self-contained — readable without opening WORKLOG_ARCHIVE.md or CI.)

- Commands / checklist:
- Result (pass/fail):
- CI run link (if available):

## Exceptions

(One-time exceptions granted during this release, if any. Reference WORKLOG decisions.)

- <none or list>

## Known limitations / follow-ups

- ...

## References

(PRs, issues, coordination threads, external links — if applicable.)

- ...
```

Release records are **permanent artifacts**, not scratch docs. They are not subject to §5b's stale-doc cleanup rule.

### Step B — Archive + reset

**Archive** (preserve full history):

1. Move **all remaining log entries** for this release from `WORKLOG.md` → `## Log` into `WORKLOG_ARCHIVE.md` under a header: `## Release vX.Y.Z (YYYY-MM-DD)`. Do not curate or select — archive everything.
2. Add an entry to the `## Releases` index at the top of `WORKLOG_ARCHIVE.md`:
   - release id, date, and link to the release record (`docs/releases/release-vX.Y.Z.md`).

**Reset** (prepare for next release):

Reset each `WORKLOG.md` snapshot section for the new working surface:

| Section             | Reset behavior                                                                                                                                                                |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `## Goal`           | Unchanged (still from `SEED.md`; update if SEED is amended for the next release)                                                                                              |
| `## Status`         | "Released vX.Y.Z on YYYY-MM-DD. Next release: planning / not started."                                                                                                        |
| `## Next actions`   | Fresh list for next release (e.g., "Owner: confirm scope for next release", "Agent: create tasks for vX.Y.(Z+1)").                                                            |
| `## Open questions` | Prune resolved entries. Carry forward still-open items, labeled `[carry-over from vX.Y.Z]`.                                                                                   |
| `## Plan`           | Clear completed items. Seed with next-release planning steps if known.                                                                                                        |
| `## Tasks`          | Remove completed tasks. Carry forward deferred tasks, explicitly labeled `[carry-over from vX.Y.Z]`.                                                                          |
| `## Proof`          | Reset `### Last known result` to blank. Pointer to `README.md` remains unless the proof mechanism itself is changing.                                                         |
| `## Decisions`      | Archive release-specific decisions into the release record (Step A). Carry forward architectural and cross-cutting decisions that affect future work, labeled `[carry-over]`. |
| `## Lessons`        | **Persist.** Lessons are institutional memory and survive across releases. Continue normal append-only / archive-at-15 behavior.                                              |
| `## Practices`      | **Persist.** Practices are institutional memory and survive across releases. Continue normal append-only / archive-at-15 behavior.                                            |
| `## Working set`    | Clear.                                                                                                                                                                        |
| `## Coordination`   | Unchanged (if external tool is still in use).                                                                                                                                 |
| `## Log`            | Note archive cutoff: "Entries through vX.Y.Z archived to WORKLOG_ARCHIVE.md." Start fresh.                                                                                    |

After reset, `WORKLOG.md` should be a clean, lightweight dashboard ready for the next cycle.

### SEED across releases

`SEED.md` describes the **project**, not a single release. It persists across releases and is not reset or recreated during closeout.

- If the next release changes Vision, Constraints, or Non-goals → use the SEED amendment process (§0).
- If it doesn't → no SEED change needed. New scope lives in `WORKLOG.md` → `## Plan` / `## Tasks`.

**SEED consolidation (optional):** when accumulated amendments make `SEED.md` hard to read, the Owner may approve a consolidation — rewriting `SEED.md` to reflect current project reality. When consolidating:

1. Archive the pre-consolidation `SEED.md` text into the most recent release record (`docs/releases/release-<id>.md`) under `## Pre-consolidation SEED`.
2. Rewrite `SEED.md` incorporating all prior amendments. Preserve the current `## Guardrails` and `### Process knobs` sections as-is (they are already current).
3. Note the consolidation in `## Amendments`: "Consolidated through vX.Y.Z — YYYY-MM-DD."

Consolidation requires Owner approval. The rewritten SEED becomes the new baseline.

---
