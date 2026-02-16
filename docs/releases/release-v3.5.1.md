# Release v3.5.1

- **Date:** 2026-02-16
- **Tag / commit:** v3.5.1 / (pending)

## Scope

- Included:
  - Modularized playbook into `docs/playbook/` (12 section files)
  - `SEED-Method.md` rewritten as kernel + index with stubs
  - Compact agent-agnostic `AGENTS.md` kernel (~2.5 KB)
  - `CLAUDE.md` and `GEMINI.md` shims (import `AGENTS.md`)
  - Distribution builds: `dist/AGENTS.kernel.md` and `dist/AGENTS.md`
  - Generator + check scripts: `build-dist.py`, `check-dist.py`,
    `build-skill.py`, `check-skill.py`
  - skills.sh skill at `skills/seed/` (`SKILL.md` + `PLAYBOOK.md`)
  - README expanded: Quick Start (kernel-first), per-agent setup, skill install
  - Dogfood guardrail in `SEED.md`
  - Removed stray YAML frontmatter from `SEED-Method-Cookbook.md`
  - Removed legacy `SEED-Method-compact.md` and `SEED-Method-compact-v2.md`
- Excluded / deferred:
  - No playbook content changes (methodology unchanged from v3.5)
  - CLI tooling (non-goal)

## Proof summary

- `./scripts/check-dist.py`: PASS (both full and kernel variants)
- `./scripts/check-skill.py`: PASS (SKILL.md + PLAYBOOK.md)
- Full markdown link/anchor/import integrity check: PASS (27 files, 0 broken)
- SEED Method audit (§7): 5/6 phases PASS, 1 PARTIAL (worklog — resolved);
  4/5 state clarity CLEAR, 1 UNCLEAR (resolved); 3 guardrail violations found
  and resolved (2 housekeeping-safe applied, 1 recorded as Owner decision)
- Result: PASS

## Exceptions

- Default guardrail 7 ("No generated files in git") overridden: generated dist
  and skill files committed because the project has no CI pipeline and consumers
  need them in the repo. Freshness enforced by check scripts. Recorded in
  `WORKLOG.md` → `## Decisions`.

## Known limitations / follow-ups

- None

## References

- Repository: https://github.com/jveres/The-SEED-Method
- Skill page: https://skills.sh/jveres/The-SEED-Method/seed
