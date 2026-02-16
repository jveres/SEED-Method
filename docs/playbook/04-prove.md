## 4) Prove phase (oracles over opinions)

A change is **meaningful** if it alters observable output, user-facing behavior, API contract, or data handling. Refactors that preserve all observable behavior do not require new proof but must not break existing proof.

**Examples of meaningful changes (proof required):**

- changing CLI flags, arguments, or exit codes
- altering API response shape or status codes
- modifying DB schema or query behavior
- changing auth/session handling
- changing file formats, serialization, or default configs
- adding or changing network access or data persistence

**Examples of usually non-meaningful changes (no new proof needed, but existing proof must stay green):**

- renaming/refactoring with identical outputs
- formatting, comments, documentation-only edits
- reordering internal logic without changing observable behavior

For each meaningful behavior, there must be proof.

Preferred:

- automated tests

Acceptable when automation isn't practical:

- built-in self-test mode
- explicit manual checklist steps (clear, reproducible)

Proof must be:

- easy to run
- documented in `README.md` (canonical); referenced from `WORKLOG.md` as pointer only (see §5)
- kept in sync with behavior changes

### When proof cannot run

If proof infrastructure is broken (CI down, tooling unavailable, environment issue), the agent must:

1. Document in `WORKLOG.md` → `## Open questions` as `[risk]`. In multi-agent mode, contributing agents post this via the coordination mechanism; the coordinator integrates it into `WORKLOG.md`.
2. Not merge to main or close tasks until proof is run and recorded.
3. Commits may continue on a branch — but the branch is not merge-eligible until proof passes.
4. If no branch work is possible, enter idle housekeeping (§5a).

The Owner may explicitly approve merging without proof as a one-time exception (see §6.1).

### Non-functional requirements gate (optional)

When SEED Constraints specify non-functional requirements (performance budgets, accessibility standards, security posture, privacy rules), add explicit proof or checklist items for those requirements. Document them alongside functional proof.

---
