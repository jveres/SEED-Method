## 6) Adapt phase (owner checkpoints)

At natural boundaries (milestone completion, direction uncertainty, scope edge), pause and present the Owner with a review guide.

Do not ask the Owner for numeric scores, ratings, or satisfaction metrics. The review guide and the Owner's own words are the feedback mechanism.

### 6.1 Approvals and exceptions

**Approval format:** Owner approvals must be explicit in writing (chat message, issue comment, or PR review). Examples: "Approved," "Yes — bundle A/B/C," "Go ahead with X." Silence or ambiguity is not approval. If unsure whether approval was given, ask.

**One-time exceptions:** When the Owner approves a one-time exception (merge without proof, temporary guardrail violation, scope deviation), record it in `WORKLOG.md` → `## Decisions` with the exception scope and reference it in the relevant log entry. Exceptions do not modify `SEED.md` — they are point-in-time waivers. If an exception effectively changes Vision, Constraints, or Non-goals (even temporarily), treat it as a `SEED.md` amendment (§0), not a one-time exception.

### Review guide (required at each checkpoint)

Address participants by name (from `## Participants`), not by role label.

Include in the checkpoint message:

1. **How to see it:** exact commands, URLs, or steps to observe the current state. Assume the Owner hasn't run anything since the last checkpoint. Include prerequisites if any.
2. **What to look at:** specific things to try, read, or poke at. Point to concrete files, screens, or outputs — not abstract dimensions.
3. **Current state vs. done:** what works now, what's not yet built, what's rough. Frame relative to SEED Vision so the Owner can gauge progress.
4. **What you want feedback on:** specific open questions where Owner input would change the next chunk. Prioritize decisions that are cheap to change now and expensive later.
5. **Guardrail proposals (if any):** lessons that should be promoted to guardrails (see §11 → Promotion).
6. **Practice promotions (if any):** practices that have proven effective across multiple chunks and should be promoted to the project skill (see §11a).

### Acting on feedback

If the Owner provides feedback:

- Actionable friction → address in the next chunk
- Process preference → record in `SEED.md` → `### Process knobs`
- Scope change → follow SEED amendment process (§0)
- New guardrail → add to `SEED.md` → `## Guardrails` with source tag (see §11)
- New skill practice → add to project skill file (see §11a)
- "Looks good, continue" → continue

Note feedback and resulting actions in the current `WORKLOG.md` log entry.

### Persist approved adaptations

If the Owner approves a process change:

- record it in `SEED.md` → `## Clarifications` → `### Process knobs`
- mention it in the latest `WORKLOG.md` log entry (so it's auditable)

### Change attribution rule

In Adapt iterations, prefer **one major change** per iteration to preserve attribution, unless the Owner explicitly approves bundling.

Bundling multiple major changes is allowed only if:

- the agent lists the exact bundled items before implementing, and
- the Owner explicitly approves the bundle (e.g., "yes, bundle improvements").

---
