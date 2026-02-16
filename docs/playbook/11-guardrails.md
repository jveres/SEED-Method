## 11) Guardrails (enforced rules that evolve)

Guardrails are rules that are always checked — at every chunk (DoD), every audit, and every release. Unlike lessons (advisory) or constraints (static), guardrails accumulate over the life of a project.

### Three sources

| Source            | Where recorded              | Who adds                                                           |
| ----------------- | --------------------------- | ------------------------------------------------------------------ |
| **Default**       | This playbook (below)       | Ship with playbook; always active unless SEED explicitly overrides |
| **Owner-imposed** | `SEED.md` → `## Guardrails` | Owner, at any time                                                 |
| **Learned**       | `SEED.md` → `## Guardrails` | Agent proposes, Owner approves                                     |

### Default guardrails

These are always active unless `SEED.md` explicitly overrides a specific guardrail.

1. **No secrets in git** — never commit credentials, API keys, tokens, or other sensitive data. Use `.env` + `.gitignore`. _(Non-negotiable — cannot be overridden.)_
2. **Proof passes before commit** — if proof exists, run it before committing when feasible. If proof cannot run due to infrastructure/tooling outage, commits may proceed on a branch, but must not merge to main or close tasks until proof is run and recorded. If no proof exists yet, the first commit must include at least an initial proof mechanism (even minimal). All subsequent commits must keep proof green.
3. **Single canonical source (avoid divergence)** — for any spec, config, or decision, designate one canonical location. Other files may summarize or reference it, but must not introduce new details that can drift. (`WORKLOG.md` `## Proof` is a pointer to `README.md`, not a copy — see §5.)
4. **Dependencies require justification** — every external dependency added must be recorded in `## Decisions` with rationale. Prefer fewer dependencies.
5. **No orphan artifacts** — every file in the repo must be referenced from `WORKLOG.md` (working set or open questions), `README.md`, or project source. Unreferenced files are deleted or referenced. Release records (`docs/releases/`) are referenced from the `## Releases` index in `WORKLOG_ARCHIVE.md`.
6. **Repo organization** — required artifacts (`SEED.md`, `README.md`, `WORKLOG.md`, `AGENTS.md`, and `WORKLOG_ARCHIVE.md` / `SEED_REQUEST.md` when present) in repo root. Scratch docs in `docs/`. Release records in `docs/releases/`. No loose files in root beyond required artifacts and standard project config (e.g., `package.json`, `Makefile`, `.gitignore`).
7. **No generated files in git** — do not commit build artifacts, derived files, or files generated from scratch unless SEED explicitly requires it. Lockfiles that ensure reproducible builds (e.g., `package-lock.json`) are allowed.
8. **Naming conventions** — project and source files: kebab-case. Scratch docs: `docs/<type>-<topic>.md`. Release records: `docs/releases/release-<id>.md`. Branches: `task/<id>-<slug>`. Playbook-mandated artifact names (`README.md`, `WORKLOG.md`, `WORKLOG_ARCHIVE.md`, `SEED.md`, `SEED_REQUEST.md`, `AGENTS.md`) are exempt. Follow language/ecosystem conventions when they conflict. Be consistent within the project.
9. **Derived data is computed, not hand-maintained** — values derivable from source (counts, statistics, generated indexes) should be produced by script or build step, not manually updated across files. When automation is impractical, designate one canonical location for the value; other files reference it. Never maintain the same derived value in multiple places by hand.

### Overriding a default guardrail

If a SEED requires overriding a default guardrail (except #1, which is non-negotiable):

- State the override explicitly in `SEED.md` → `## Guardrails` with rationale.
- The override applies only to the stated guardrail. All others remain active.

### Promotion: lesson → guardrail

When a lesson in `## Lessons` represents a mistake that is significant enough to enforce (cost real time, broke things, or is likely to recur):

1. Agent proposes the guardrail at the next owner checkpoint (§6), stating:
   - the lesson it comes from
   - the proposed guardrail wording (one line, actionable)
   - why advisory isn't enough (what goes wrong if it's ignored)
2. Owner approves or rejects.
3. If approved: add to `SEED.md` → `## Guardrails` with source tag `[learned]` and date.
4. The original lesson may remain in `## Lessons` or be pruned — the guardrail is now the enforced version.

### Project-specific guardrails in `SEED.md`

Each entry includes:

- The rule (one line, actionable)
- Source tag: `[owner]` or `[learned]`
- Date added

Example:

```md
## Guardrails

- No direct database queries outside the repository layer — all access through `db/` module. [owner] 2025-01-15
- Always validate webhook signatures before processing payload — skipping this caused a 2-hour debug session. [learned] 2025-02-01
- Maximum 3 external API calls per user-facing request — performance budget. [owner] 2025-01-15
```

---


## 11a) Practice promotion (best practices that evolve)

Practices are the positive counterpart to guardrails. Where guardrails prevent mistakes from recurring, practices ensure successes are repeated. Together they form the complete learning system:

```
Negative:  Mistake  → Lesson   → Guardrail  (project-enforced, prevents recurrence)
Positive:  Success  → Practice → Skill      (cross-project portable, enables reuse)
```

### Promotion: practice → skill

When a practice in `## Practices` has proven effective across multiple chunks, contexts, or projects, and represents reusable knowledge:

1. Agent proposes promotion at the next owner checkpoint (§6), stating:
   - the practice it comes from
   - why it's generalizable (not just situational)
   - proposed wording for the skill entry
2. Owner approves or rejects.
3. If approved: add to the project's skill file (e.g., `SKILL.md`) or to an organizational skill library, with source tag `[learned]` and date.
4. The original practice may remain in `## Practices` or be pruned — the skill entry is now the reusable version.

### What makes a practice promotable

Not every practice should become a skill. Promotion criteria:

- **Proven across contexts** — worked in more than one chunk, task type, or module. A pattern that worked once might be coincidence.
- **Generalizable** — applicable beyond this specific project. "Use Redis for caching" is project-specific; "define cache interface before choosing implementation" is generalizable.
- **Teachable** — can be explained in 1–2 lines clearly enough that a new agent can apply it without additional context.
- **Not already a process knob or guardrail** — process preferences go in `### Process knobs`; enforced rules go in `## Guardrails`. Skills are advisory best practices.

### Skill entry format

Each promoted practice in the skill file includes:

- The practice (one line, actionable)
- Source tag: `[learned]`
- Date promoted
- Origin (optional): project or context where it was discovered

Example:

```md
- Write API contract as a scratch doc before implementation — eliminates integration back-and-forth. [learned] 2025-03-15
- Run proof after every 2-3 file changes, not just per chunk — catches regressions 10x faster. [learned] 2025-04-01
- Split middleware into pure transform + side-effect layers — each independently testable. [learned] 2025-04-20
```

---

# Appendix — Skeletons

The skeleton templates are stored in `docs/playbook/12-appendix-skeletons.md`
to keep `SEED-Method.md` smaller for day-to-day reading and agent ingestion.

See [12-appendix-skeletons.md](12-appendix-skeletons.md).
