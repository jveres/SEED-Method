## 5) Worklog phase (snapshot + log in one file; required)

`WORKLOG.md` is the single handover artifact — and the Owner's dashboard. It combines a bounded current-state snapshot with an append-only log.

### Structure

`WORKLOG.md` has two regions:

1. **Snapshot sections** (top) — rewritten each chunk to reflect current state
2. **Log section** (bottom) — append-only dated entries

### Snapshot sections (rewrite each chunk)

Snapshot sections are organized into two clusters:

**Dashboard cluster (first screenful — "where are we, what's next, what's blocked"):**

- Goal (current interpretation of `SEED.md`)
- Current status (done / in progress / not started)
- Next actions (concrete, ordered)
- Open questions (risks, unknowns, research needs, hardening items — see below)

**Detail cluster (reference material — "how, why, what exactly"):**

- Plan (short sequence)
- Tasks (numbered; keep numbering stable where possible; dependency annotations allowed)
- Proof (pointer to `README.md` + environment notes + last known result)
- Decisions made (and why)
- Lessons (hard-won knowledge; append-only — see below)
- Practices (effective patterns; append-only — see below)
- Working set (files touched, branch/commit if applicable)
- Coordination (if external tool is in use: tool name + project location or key link pattern)

If SEED includes explicit compatibility targets (platforms/browsers/versions):

- Include a **Compatibility check status** section stating what has been verified and what remains.

### Proof steps: canonical location

`README.md` is the canonical and only location for proof steps. `WORKLOG.md` `## Proof` is a pointer — it references `README.md` and records environment notes (e.g., local quirks, runtime workarounds) and the last known result. Do not duplicate proof steps in `WORKLOG.md`.

### Lessons section (append-only within snapshot)

Unlike other snapshot sections, `## Lessons` is not rewritten each chunk. Entries are added at time of discovery and preserved across rewrites.

Each entry is a single concise line:

- what was learned
- why it matters (or what to avoid)

When the list exceeds ~15 entries, move the least-relevant ones to the top of `WORKLOG_ARCHIVE.md` under `## Archived lessons`. Note the move in the current log entry.

What goes in `## Lessons`:

- Failed approaches and why they failed
- Non-obvious system/API/environment behaviors
- Gotchas that cost time
- Anything an agent would want to tell the next agent: "don't repeat my mistake"

What doesn't go in (already has a home):

- Architectural choices → `## Decisions`
- Process preferences → `SEED.md` → `### Process knobs`
- Recurring mistakes worth enforcing → `SEED.md` → `## Guardrails` (see §11 → Promotion)
- Effective patterns worth repeating → `## Practices`
- Current open loops → `## Open questions`

### Practices section (append-only within snapshot)

Like `## Lessons`, `## Practices` is append-only — entries are added at time of discovery and preserved across rewrites. Where Lessons capture what went wrong, Practices capture what went right.

Each entry is a single concise line:

- what was done
- why it worked well (or what it enabled)

When the list exceeds ~15 entries, move the least-relevant ones to `WORKLOG_ARCHIVE.md` under `## Archived practices`. Note the move in the current log entry.

What goes in `## Practices`:

- Approaches that proved effective and are worth repeating
- Patterns that solved a class of problems, not just one instance
- Techniques that improved speed, quality, or clarity
- Anything an agent would want to tell the next agent: "do this again"

What doesn't go in (already has a home):

- Architectural choices → `## Decisions`
- Process preferences → `SEED.md` → `### Process knobs`
- Patterns worth standardizing across projects → promote to project skill (see §11a)
- Mistakes and gotchas → `## Lessons`

### Open questions section (replaces Risks / unknowns)

Captures anything unresolved: risks, unknowns, research needs, hardening items, things to verify before release.

Each entry has a type tag and status:

- Type tags: `[risk]`, `[question]`, `[hardening]`, `[verify]`
- Statuses: `OPEN`, `RESEARCHING` (with pointer to scratch doc if applicable), `RESOLVED`, `→ Task N`

Example:

```md
## Open questions

- [risk] Concurrent writes could corrupt state — no locking yet → OPEN
- [question] Which auth library fits offline constraint? → RESEARCHING, see docs/research-auth.md
- [hardening] Input validation missing on all endpoints → → Task 12
- [verify] Does Safari support the CSS grid we're using? → RESOLVED, yes (see Decisions)
```

When resolved, the conclusion feeds into its destination:

- `## Decisions` (if a choice was made)
- `## Lessons` (if something was learned)
- `## Tasks` (if work was identified)
- Or marked `RESOLVED` with a one-line answer inline

Resolved entries may be pruned during snapshot rewrites — the resolution lives in its destination.

### Log section (append each chunk)

Each chunk/session must append one entry to `## Log` including:

- date (YYYY-MM-DD), agent role and session name (e.g., `builder / StarNova`), and short summary
- descriptive hash tags
- what changed (high level)
- what proof was run / observed
- what's next
- owner feedback and actions taken (if checkpoint occurred)

**Lightweight format (non-behavioral chunks):**

Chunks with no behavioral changes (housekeeping, doc fixes, archive moves, formatting) may use a condensed format:

```md
### YYYY-MM-DD — <short title> (<role> / <session name>)

Housekeeping only. No behavioral changes. <what was done>. Proof: unchanged, still passing.
```

Use the full template for any chunk that alters observable output or requires new proof.

### Archive trigger

When the log exceeds ~10 entries, move older entries to `WORKLOG_ARCHIVE.md`, keeping the most recent 5 entries in `WORKLOG.md`. Note the archive cutoff date at the top of `## Log`.

---


## 5a) Housekeeping (idle time)

When implementation cannot proceed — waiting for owner feedback, blocked on a dependency, waiting for CI, or direction is unclear — use the time for housekeeping.

### Edit categories

- **Housekeeping-safe (allowed during idle):** doc drift fixes, formatting, archive moves, clarifying existing proof steps without changing behavior, stale reference cleanup, comment/typo fixes.
- **Behavioral (not allowed during idle):** code changes, dependency changes, new or modified proof, architectural changes — anything that alters observable output or requires new proof.

### Allowed during idle

In priority order:

1. **Freshen `WORKLOG.md`** — ensure snapshot sections reflect current state; catch any missed log entries.
2. **Run proof** — verify existing proof still passes; record result in `## Proof` → `### Last known result`.
3. **Check guardrails** — scan for violations of default (§11) and project-specific (`SEED.md` → `## Guardrails`) guardrails; fix or flag.
4. **Check archive triggers** — if log exceeds ~10 entries or lessons/practices exceed ~15, archive now.
5. **Audit `README.md`** — verify run/prove instructions match current behavior; fix drift (housekeeping-safe only).
6. **Self-audit** — run the playbook audit protocol (§7) and note any deviations in `## Open questions` or address them directly if they are housekeeping-safe fixes (e.g., missing log entry, stale working set).
7. **Review `## Lessons`** — check for relevance; consolidate duplicates; consider whether any should be promoted to guardrails.
8. **Review `## Practices`** — check for relevance; consolidate duplicates; consider whether any should be promoted to the project skill (see §11a).
9. **Review `## Open questions`** — check for stale entries; prune resolved items; flag items that need owner input.
10. **Clean working tree** — remove dead files, fix stale gitignore entries, ensure no secrets are tracked.

### Not allowed during idle

- Starting new tasks or features
- Behavioral edits (see categories above)
- Adding dependencies
- Expanding scope
- Making architectural changes

**Idle housekeeping must not produce behavioral changes that haven't been planned and claimed.** If housekeeping reveals work that should be done, add it to `## Tasks` — don't do it.

---


## 5b) Scratch docs (working documents)

For exploration that doesn't fit in a single `## Open questions` entry, create a working document.

**Location:** `docs/`

**Naming:** `docs/<type>-<topic>.md` where type is one of:

- `spike` — technical exploration / proof of concept
- `research` — comparison, market research, options analysis
- `design` — design alternatives, architecture options

**Lifecycle:**

1. Create when an open question needs extended exploration.
2. Reference from `## Open questions` while active.
3. Track in `## Working set` while active.
4. On resolution: conclusion feeds into `## Decisions`, `## Lessons`, or `## Tasks`.
5. Keep the doc as reference or delete it. Do not accumulate stale scratch docs.

**Scratch docs are supporting material. The conclusion must land in `WORKLOG.md`.**

Release records (`docs/releases/release-<id>.md`) are **not** scratch docs. They are permanent artifacts with their own lifecycle — see §10a.

---
