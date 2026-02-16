# WORKLOG

<!-- Dashboard cluster: first screenful — where are we, what's next, what's blocked -->

## Goal (from `SEED.md`)

Make the SEED Method publicly available and reusable by anyone on GitHub.

## Status

- Released v3.5.1 on 2026-02-16.
- Next release: planning / not started.

## Next actions

1. Owner: confirm scope for next release.

## Open questions

(None.)

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

- Date:
- Result:
- Notes:

## Decisions

- Generated dist and skill files committed to git — this project has no CI
  pipeline and consumers need the built artifacts (`dist/`, `skills/`) in the
  repo. Overrides default guardrail 7 ("No generated files in git").
  Freshness is enforced by `scripts/check-dist.py` and
  `scripts/check-skill.py`. [carry-over]
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

(Clean.)

---

## Log

Entries through v3.5.1 archived to WORKLOG_ARCHIVE.md.
