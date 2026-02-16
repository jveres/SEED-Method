## 3) Build phase (full-speed execution)

Work in increments ("chunks") that are:

- **verifiable** (proof improves each chunk)
- **revertible** (clean commits or clear rollback)

A chunk is the smallest unit of work that produces a verifiable change. Aim for 1–3 tasks per chunk. If a chunk takes more than one focused session, consider splitting.

In multi-agent mode, a "chunk" maps to one integration event into the baseline (e.g., one merged PR or one coordinated merge set). Individual contributing-agent sessions are captured as handoff notes (§9.8), not as separate chunks.

Prefer finishing the delivery over adding extras not required by SEED.

### 3.1 Chunk Definition of Done (DoD)

A chunk is "Done" only when:

- the deliverable matches SEED scope for that chunk
- proof exists/updated for changed behavior (tests/self-test/checklist)
- proof has been executed and the result recorded:
  - **local run:** command + exit code / key output
  - **CI run:** workflow name + run identifier or link + pass/fail
  - **manual check:** date + pass/fail + notes
- no guardrail violations (default §11 + project-specific in `SEED.md` → `## Guardrails`)
- `WORKLOG.md` snapshot sections are updated (dashboard: status, next actions, open questions; detail: plan/tasks status, proof, decisions, working set)
- `WORKLOG.md` has a new log entry for the chunk
- any hard-won lessons from this chunk are recorded in `WORKLOG.md` → `## Lessons`
- any effective practices discovered in this chunk are recorded in `WORKLOG.md` → `## Practices`

### 3.2 Recovery play (failed chunk)

If a chunk fails partway and cannot be quickly fixed:

1. Revert to the last known-good commit (or clearly mark partial changes).
2. Document the failure in a `WORKLOG.md` log entry (what failed, why, what was attempted).
3. Update `WORKLOG.md` → `## Open questions` with the failure context.
4. Consider whether the failure should become a guardrail — if the mistake is likely to recur, propose a new guardrail at the next owner checkpoint (see §11 → Promotion).
5. Check whether anything _did_ work well before the failure — record those in `## Practices` even if the chunk overall failed.
6. Re-plan: adjust tasks or approach before retrying.

---
