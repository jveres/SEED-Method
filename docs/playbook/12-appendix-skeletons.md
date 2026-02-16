# Appendix — Skeletons (all referenced artifacts)

## A) `SEED.md` skeleton

```md
# SEED

## Participants

(Owner names are stable identifiers. Agent names are session-scoped and may change
on renewal — use role labels for cross-session traceability. Platform records the
typical orchestrator · model; actual per-session values go in log entries when they differ.)

| Role          | Name/Handle   | Platform                 | Notes |
| ------------- | ------------- | ------------------------ | ----- |
| Owner         |               | —                        |       |
| Agent: <role> | (per session) | <orchestrator> · <model> |       |

## Vision (Owner wording)

(1–3 sentences. What should exist when done?)

## Success criteria

(What does a great result look like? What matters most?)

- ...
- ...
- ...

## Constraints

(Tech choices, offline/no-network, dependency policy, single-file, platforms, perf budgets, etc.)

- Constraint:
- Constraint:

## Guardrails

(Enforced rules. Default guardrails from AGENTS.md §11 are always active. Add project-specific guardrails here. Tag each with source and date.)

(To override a default guardrail, state it explicitly here with rationale. Default #1 — no secrets in git — cannot be overridden.)

- Guardrail. [owner/learned] YYYY-MM-DD
- Guardrail. [owner/learned] YYYY-MM-DD

## Non-goals

(Explicitly out of scope.)

- Non-goal:
- Non-goal:

## Stop conditions

(When to pause and ask before proceeding.)

- Stop if:
- Stop if:

## Timeline / urgency

(Deadline, pace expectation, or "no deadline".)

- Timeline:

## Clarifications

(Only necessary clarifications; keep Owner's wording above intact.)

- Clarification:

### Process knobs

(Approved adaptations that become new defaults for this repo.)

- Knob:
  - Setting:
  - Why:
  - Since (YYYY-MM-DD):

## Amendments

(Owner-approved scope changes after initial SEED, with date and rationale. If consolidated, note: "Consolidated through vX.Y.Z — YYYY-MM-DD." See §10a.)

- Amendment (YYYY-MM-DD):
  - Change:
  - Rationale:
```

---

## B) `SEED_REQUEST.md` skeleton

```md
# SEED REQUEST

Owner input is required before implementation can begin.

## Questions (answer in order)

1. Vision: what should exist when done?
2. Success criteria: what does a great result look like? What matters most?
3. Constraints: any hard requirements?
4. Non-goals: anything explicitly out of scope?
5. Stop conditions: when should we pause and ask you?
6. Timeline or urgency: any deadline or pace expectation?

## Assumptions (UNAPPROVED)

(Only fill this if helpful; do not implement based on these.)

- Assumption:
- Assumption:
```

---

## C) `README.md` skeleton (minimal "run + prove")

```md
# <Project Name>

## What this is

(1–3 sentences aligned with `SEED.md` Vision.)

## How to run

- Prereqs:
- Install:
- Run:

## How to prove it works

(Prefer a single command; otherwise a short checklist.)

- Automated:
  - Command:
  - Expected:
- Manual (if needed):
  1.
  2.
  3.

## Notes

- Constraints:
- Known limitations:
```

---

## D) `WORKLOG.md` skeleton (snapshot + log; required)

```md
# WORKLOG

<!-- Dashboard cluster: first screenful — where are we, what's next, what's blocked -->

## Goal (from `SEED.md`)

- ...

## Status

- Done:
- In progress:
- Not started:

## Next actions

1.
2.
3.

## Open questions

(Type tags: [risk], [question], [hardening], [verify]. Statuses: OPEN, RESEARCHING, RESOLVED, → Task N. Prune resolved entries during snapshot rewrites.)

- ...

<!-- Detail cluster: reference material — how, why, what exactly -->

## Plan

1.
2.
3.

## Tasks

(Keep numbering stable where possible. Dependency annotations allowed, e.g., "blocked by Task 1".)

1. [ ] ...
2. [ ] ...
3. [ ] ...

## Proof

See [README.md → How to prove it works](README.md#how-to-prove-it-works)

### Environment notes

- (Local quirks, runtime workarounds, or agent-specific setup — if any)

### Last known result

- Date (YYYY-MM-DD):
- Result (local / CI link):
- Notes:

## Decisions

- Decision:
  - Why:
  - Decided by: <participant name>

## Lessons

(Append-only. One line per lesson. Do not remove during snapshot rewrites. Archive to `WORKLOG_ARCHIVE.md` when list exceeds ~15 entries. If a lesson is significant enough to enforce, propose promotion to guardrail — see §11.)

- ...

## Practices

(Append-only. One line per practice. Do not remove during snapshot rewrites. Archive to `WORKLOG_ARCHIVE.md` when list exceeds ~15 entries. If a practice is proven and generalizable, propose promotion to project skill — see §11a.)

- ...

## Working set

- Files touched:
- Branch:
- Commit:
- Environment notes (if relevant; e.g., tools installed, runtime workarounds):

## Coordination

(Only when external coordination tool is in use. Remove this section if not applicable.)

- Tool:
- Location / link:

---

## Log

(Append-only. Keep most recent ~5 entries here. When log exceeds ~10 entries, archive older entries to `WORKLOG_ARCHIVE.md` and note cutoff date below.)

### YYYY-MM-DD — <short title> (<role> / <session name> · <model if different from default>)

**Summary**

- ...

**Changes**

- ...

**Proof run**

- Command/steps:
- Expected:
- Observed:

**Decisions**

- Decision:
  - Why:
  - Decided by: <participant name>

**Next**

1.
2.
3.

**Feedback from <participant name> (if checkpoint occurred)**

- Feedback:
- Action taken:
```

---

## E) `WORKLOG_ARCHIVE.md` skeleton

```md
# WORKLOG ARCHIVE

## Releases

(Index of all release records. One line per release.)

| Release | Date       | Record                                                             |
| ------- | ---------- | ------------------------------------------------------------------ |
| vX.Y.Z  | YYYY-MM-DD | [docs/releases/release-vX.Y.Z.md](docs/releases/release-vX.Y.Z.md) |

---

## Archived lessons

(Overflow from WORKLOG.md ## Lessons when list exceeds ~15 entries.)

- ...

## Archived practices

(Overflow from WORKLOG.md ## Practices when list exceeds ~15 entries.)

- ...

---

(Archived log entries below, most recent release first.)

## Release vX.Y.Z (YYYY-MM-DD)

(Final snapshot sections and all log entries for this release, moved here during §10a closeout.)

### YYYY-MM-DD — <short title>

...
```

---

## F) Release record skeleton

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

## Pre-consolidation SEED

(Only present if SEED was consolidated at this release. Full text of previous SEED.md preserved for audit trail.)
```

---

## G) `.env.example` skeleton (if needed)

```bash
# Copy to .env (do not commit .env)
# Add only non-secret defaults here; document secrets clearly.

# EXAMPLE_VAR=
```

---

## H) `.gitignore` snippet (minimum for secrets)

```gitignore
.env
.env.*
!.env.example
```
