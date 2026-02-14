---
name: seed-method
description: >
  The SEED Method is a development methodology for agent-driven projects.
  Use this skill when working on any project that follows SEED Method discipline —
  it defines phases, artifacts, coordination, guardrails, and adaptation patterns
  for single-owner, multi-agent delivery.
---

# SEED Method Cookbook

Practical patterns for adapting the SEED Method to real-world situations. This document is a **companion reference**, not part of the playbook itself. The playbook (`AGENTS.md`) defines the workflow. This cookbook shows how to apply it when the defaults don't quite fit.

Each recipe follows the same shape: **Situation → Problem → Pattern → What to record.**

---

## Table of Contents

1. [Monorepo with multiple packages](#1-monorepo-with-multiple-packages)
2. [Retrofitting onto an existing codebase](#2-retrofitting-onto-an-existing-codebase)
3. [Tiny one-shot projects](#3-tiny-one-shot-projects)
4. [Long-running projects with many releases](#4-long-running-projects-with-many-releases)
5. [Owner is also the agent](#5-owner-is-also-the-agent)
6. [New agent picking up mid-project](#6-new-agent-picking-up-mid-project)
7. [Working without git](#7-working-without-git)
8. [UI and visual projects (proof is hard)](#8-ui-and-visual-projects-proof-is-hard)
9. [Libraries vs. applications](#9-libraries-vs-applications)
10. [Spikes and research that might not ship](#10-spikes-and-research-that-might-not-ship)
11. [CI integration](#11-ci-integration)
12. [Multiple Owners or stakeholders](#12-multiple-owners-or-stakeholders)
13. [WORKLOG is getting unwieldy](#13-worklog-is-getting-unwieldy)
14. [Ambiguous or evolving SEED](#14-ambiguous-or-evolving-seed)
15. [Agent-to-agent handoff (relay pattern)](#15-agent-to-agent-handoff-relay-pattern)
16. [Partial adoption (introducing the SEED Method gradually)](#16-partial-adoption-introducing-the-seed-method-gradually)
17. [Named participants and identity](#17-named-participants-and-identity)
18. [Collecting and promoting best practices](#18-collecting-and-promoting-best-practices)
19. [High-velocity projects (multiple releases per day)](#19-high-velocity-projects-multiple-releases-per-day)

---

## 1) Monorepo with multiple packages

**Situation:** One repository, multiple independently shippable packages.

**Problem:** The SEED Method's default artifact layout assumes one project per repo. A single `SEED.md` / `WORKLOG.md` at the root conflates unrelated work streams.

**Pattern A — Per-package SEED Method instances:**

Each package gets its own `SEED.md`, `WORKLOG.md`, `README.md`, and `docs/`. One shared `AGENTS.md` at the repo root.

```
repo-root/
├── AGENTS.md
├── packages/
│   ├── api/
│   │   ├── SEED.md
│   │   ├── README.md
│   │   ├── WORKLOG.md
│   │   └── docs/
│   └── web/
│       ├── SEED.md
│       ├── README.md
│       ├── WORKLOG.md
│       └── docs/
```

Use when: packages ship independently, have different timelines, or different agents.

Cross-cutting changes (e.g., shared library update that affects multiple consumers) originate in the library's task list. Downstream impact is logged as `[risk]` open questions in each affected package's `WORKLOG.md`. Integration proof must pass across all affected packages before merge.

**Pattern B — Single SEED Method instance, tagged tasks:**

One `SEED.md` and `WORKLOG.md` at the root. Tasks are tagged with their package: `Task 4 [api] — add auth middleware`.

Use when: packages share a release cadence and are tightly coupled.

**Decision guide:**

| Signal                                  | Points to           |
| --------------------------------------- | ------------------- |
| Packages ship independently             | **A** (per-package) |
| Different agents own different packages | **A**               |
| Packages have different Owners          | **A** (strongly)    |
| Packages share a single release cadence | **B** (whole-repo)  |
| Fewer than 3 packages, tightly coupled  | **B**               |
| Cross-package changes are rare          | **A**               |
| Cross-package changes are the norm      | **B**               |

**What to record:**

```md
### Process knobs

- Knob: Monorepo strategy
  - Setting: Strategy A (per-package instances) / Strategy B (single instance, tagged tasks)
  - Why: <rationale>
  - Since: YYYY-MM-DD
```

---

## 2) Retrofitting onto an existing codebase

**Situation:** A codebase already exists. No `SEED.md`, no `WORKLOG.md`, possibly no tests. You want to bring it under SEED Method discipline.

**Problem:** Bootstrap assumes a greenfield start. Demanding full compliance on day one is unrealistic for a large existing project.

**Pattern — Incremental adoption:**

1. **Write `SEED.md` as-is.** Vision describes the existing project's purpose, not a new build. Constraints reflect reality (language, framework, infra already chosen). Include a note:

   ```md
   ## Clarifications

   - This SEED describes an existing project being brought under SEED Method discipline.
     Pre-existing code is accepted as baseline; no retroactive proof required
     for unchanged behavior.
   ```

2. **Bootstrap = inventory, not scaffold.** Instead of creating a project skeleton, the bootstrap deliverables are:
   - `README.md` — how to run and prove (even if proof is minimal)
   - `WORKLOG.md` — current state, known issues, initial task list
   - An honest `## Open questions` capturing tech debt, missing tests, and unclear behavior

3. **Proof grows forward.** New or changed behavior requires proof per §4. Existing untested behavior is tracked as `[hardening]` open questions and converted to tasks over time.

4. **Guardrails apply immediately** to new work. For existing violations (e.g., secrets in git history, orphan artifacts), log them as `[hardening]` items and schedule remediation.

**What to record:**

```md
### Process knobs

- Knob: Retrofit mode
  - Setting: ON — pre-existing code is accepted baseline; proof grows forward only
  - Why: existing codebase, retroactive proof for unchanged behavior is impractical
  - Since: YYYY-MM-DD
```

---

## 3) Tiny one-shot projects

**Situation:** Single file, one-shot script, quick tool — the kind of thing where full ceremony feels absurd.

**Problem:** Creating `SEED.md`, `WORKLOG.md`, `README.md`, and `AGENTS.md` for a 50-line script is overhead that exceeds the value of the deliverable.

**Pattern — Minimum viable SEED Method:**

The playbook requires `WORKLOG.md` always. It does not require that any artifact be large. For truly tiny projects:

- **`SEED.md`:** 3–5 lines. Vision + one constraint is often enough.
- **`WORKLOG.md`:** Status, one task ("build the thing"), proof command, done. Five lines in the snapshot, one log entry.
- **`README.md`:** How to run + how to prove. Four lines.
- **Proof:** A single invocation with expected output.

The whole thing can be set up in under 2 minutes. The overhead is proportional because the _content_ is proportional.

What you **don't** skip:

- Proof (even a single command showing it works)
- The worklog entry (so handoff is clean)
- Guardrails (especially: no secrets in git)

What you **can** minimize:

- Plan (one step: "build it")
- Tasks (one task)
- Decisions (likely none)
- Open questions (likely none)

**What to record:** Nothing special. The SEED is just short.

---

## 4) Long-running projects with many releases

**Situation:** The project has been going for months. You're on v3.x. `SEED.md` has accumulated amendments. `WORKLOG_ARCHIVE.md` is extensive.

**Problem:** Accumulated history makes it hard for agents (and the Owner) to see current reality.

**Pattern — Periodic consolidation:**

1. **SEED consolidation (§10a).** When `SEED.md` amendments make it hard to read, consolidate. Archive the pre-consolidation text in the release record, then rewrite `SEED.md` to reflect current project reality.

2. **Lessons and practices pruning.** When either list passes ~15, archive less-relevant entries to `WORKLOG_ARCHIVE.md`. Promote recurring lessons to guardrails (§11). Promote proven practices to the project skill (§11a).

3. **Decisions pruning.** At each release closeout (§10a), move release-specific decisions into the release record. Carry forward only cross-cutting architectural decisions.

4. **Open questions hygiene.** At each release closeout, force-resolve or explicitly carry forward every open question. Don't let the list silently grow.

5. **Guardrail review.** Periodically check whether project-specific guardrails are still relevant. Outdated guardrails add friction without value. Owner can remove them during any checkpoint.

**Rule of thumb:** After every 3–5 releases, do a "spring cleaning" pass:

- Consolidate SEED if needed
- Review lessons for promotion or archival
- Review practices for promotion or archival
- Review guardrails for relevance
- Ensure `WORKLOG.md` is a clean dashboard, not a museum

**What to record:**

```md
### Process knobs

- Knob: Spring cleaning cadence
  - Setting: every 3 releases
  - Why: project is long-running; prevent artifact drift
  - Since: YYYY-MM-DD
```

---

## 5) Owner is also the agent

**Situation:** You're a solo developer using the SEED Method to organize your own work. You're both the Owner deciding what to build and the agent building it.

**Problem:** The Owner/agent separation feels like talking to yourself. Checkpoints, review guides, and approval ceremonies add friction with no second party.

**Pattern — Collapsed ceremony, same artifacts:**

- **SEED:** Still write it. The act of writing Vision and Constraints is valuable even when you're the only reader. It prevents scope creep against your future self.
- **Checkpoints:** Replace the review guide with a brief self-review in the log entry. Ask yourself the same questions: "Does this match the vision? Am I drifting? Any risks?"
- **Approvals:** Implicit. You don't need to write "Approved" to yourself. Record decisions directly.
- **`WORKLOG.md`:** Still the dashboard. Its value is _continuity across sessions_, not communication with another person. When you pick the project back up after a week, the worklog tells you where you are.
- **Proof:** Even more important when solo. No one else is checking your work.

What you **can** skip:

- Review guide format (§6) — use a simpler self-check
- Formal approval language
- Handoff notes (§9.8) — there's no handoff
- Coordination section in worklog

What you **don't** skip:

- `SEED.md` (you will forget what you intended)
- `WORKLOG.md` (you will forget where you stopped)
- Proof (you will break things without noticing)
- Guardrails (discipline matters more without accountability)

**What to record:**

```md
### Process knobs

- Knob: Owner-as-agent mode
  - Setting: ON — collapsed ceremony, self-review replaces formal checkpoints
  - Why: solo developer, no separate Owner
  - Since: YYYY-MM-DD
```

---

## 6) New agent picking up mid-project

**Situation:** A fresh agent (new session, different model, different person) is joining or continuing a SEED Method project.

**Problem:** The agent needs to get oriented quickly without re-reading the entire history.

**Pattern — Three-file orientation:**

The new agent reads exactly three files in this order:

1. **`SEED.md`** — what this project is, what matters, what's off-limits. Start with `## Participants` to understand who's involved and your role.
2. **`WORKLOG.md`** dashboard cluster (top four sections) — current state, what's next, what's blocked
3. **`README.md`** — how to run it, how to prove it

That's it. The agent does not need to read:

- `WORKLOG_ARCHIVE.md` (unless investigating a specific historical decision)
- `AGENTS.md` (unless the agent doesn't already know the SEED Method)
- Old log entries (unless debugging why something was done a certain way)

**`## Lessons` and `## Practices` are the shortcuts.** They're the institutional memory — the compressed "things a new agent needs to know." If both sections are well-maintained, the new agent gets the hard-won knowledge (what to avoid, what to repeat) without reading the full history.

**First action for a new agent:**

1. Read the three files above.
2. Run proof to verify the project is in a working state.
3. Check `## Open questions` for anything that might block the next task.
4. Claim a task from `## Next actions` or `## Tasks`.

If proof fails on pickup, that's a blocker — log it and resolve before doing new work.

**What to record:** Nothing in `SEED.md`. The new agent's first log entry in `WORKLOG.md` should note the pickup:

```md
### YYYY-MM-DD — Session pickup (builder / CosmicRay)

**Summary**

- Read SEED, WORKLOG, README. Ran proof — PASS.
- Continuing from Task N.
```

---

## 7) Working without git

**Situation:** The environment doesn't support git (sandboxed agent, restricted tooling, platform constraint).

**Problem:** The SEED Method references git throughout — commits, branches, tags, `.gitignore`, revert strategies. Without git, some mechanisms break.

**Pattern — File-based equivalents:**

| Git concept     | Without-git equivalent                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| Commits         | Save points. Note file state in `## Working set` with timestamps.                                       |
| Branches        | Work in a separate directory or clearly marked files. Note the "branch" in `## Working set`.            |
| Revert          | Keep a `_backup/` directory with snapshots before risky changes. Not elegant, but functional.           |
| `.gitignore`    | A `DO_NOT_SHARE.md` listing sensitive files that must not be copied or transmitted.                     |
| Tags / releases | Note the release state in the release record: "Files as of YYYY-MM-DD HH:MM" with a manifest if needed. |
| Merge conflicts | `WORKLOG.md` task ownership + file reservation (§9) is the conflict prevention mechanism.               |

**Proof still works.** Tests, self-test modes, and manual checklists don't require git.

**`WORKLOG.md` becomes even more critical** — it's the only history when there's no commit log.

**What to record:**

```md
## Constraints

- No git available. File-based version management per SEED Method Cookbook §7.
```

---

## 8) UI and visual projects (proof is hard)

**Situation:** The deliverable is a website, design system, game, visualization, or other visual artifact where "correctness" is partly aesthetic.

**Problem:** Automated tests can check structure, but they can't verify "this looks right." The playbook's proof-first principle seems hard to apply.

**Pattern — Layered proof:**

Split proof into what machines can check and what humans must check:

1. **Automated (machines):**
   - Does it build without errors?
   - Does it render without crashes?
   - Are structural expectations met? (elements exist, routes resolve, data loads)
   - Accessibility checks (axe, lighthouse)
   - Screenshot comparison / visual regression (if tooling supports it)

2. **Manual checklist (humans):**
   - Specific screens or states to eyeball
   - Specific interactions to try
   - Specific devices/browsers to check (if SEED specifies compatibility targets)

The manual checklist goes in `README.md` → "How to prove" alongside the automated commands. It must be concrete and reproducible — not "check that it looks good" but "navigate to /dashboard, verify the chart renders with sample data, check that the legend is visible on a 375px-wide viewport."

**Checkpoints matter more.** Since proof has a human-eye component, checkpoint reviews (§6) carry more weight. Include screenshots or screen recordings in checkpoint messages when possible.

**What to record:**

```md
### Process knobs

- Knob: Proof strategy
  - Setting: Layered — automated structural checks + manual visual checklist
  - Why: visual deliverable; full automation isn't feasible
  - Since: YYYY-MM-DD
```

---

## 9) Libraries vs. applications

**Situation:** The deliverable is a library (consumed by other code) rather than an end-user application.

**Problem:** Libraries don't "run" in the same way. Proof looks different. "How to prove" isn't "launch the app and click around."

**Pattern — Contract-based proof:**

- **Unit tests are the primary proof.** Each public API surface has test coverage.
- **Integration examples** (an `examples/` directory or inline doc examples) double as proof: they show usage AND verify the API works.
- **`README.md`** focuses on "how to use" (installation, import, API) rather than "how to run."
- **"How to prove"** = "how to run the test suite" + optionally "how to run examples."

For libraries with no runtime side effects, automated tests are usually sufficient — manual checklists are rarely needed.

**Versioning matters more.** Libraries have consumers who depend on stable APIs. SEED Constraints should explicitly state:

- Versioning scheme (SemVer is the strong default)
- Backward compatibility policy
- Supported platforms/runtimes

**What to record:** Usually nothing special. The SEED naturally describes a library. If backward compatibility is a constraint, state it:

```md
## Constraints

- SemVer strictly. No breaking changes in minor/patch releases.
- Support Node >= 18 and browsers with >1% global usage.
```

---

## 10) Spikes and research that might not ship

**Situation:** The Owner asks for exploration — "figure out if X is feasible," "compare approaches A and B," "prototype something and show me."

**Problem:** The deliverable isn't a shippable artifact. Standard phases (Build → Prove) don't quite apply because the output is a _decision_, not a _product_.

**Pattern — Spike as a SEED Method micro-project:**

- **`SEED.md` Vision:** "A recommendation on whether/how to do X, supported by a working prototype or clear evidence."
- **Success criteria:** "Owner can make an informed decision based on the deliverable."
- **Proof:** The prototype works (if applicable) + the recommendation is justified with evidence.
- **Primary deliverable:** A scratch doc (`docs/spike-<topic>.md`) containing findings, tradeoffs, and recommendation. Plus a prototype if applicable.

The spike follows all SEED Method phases, but they're compressed:

- Bootstrap: create the doc structure + minimal prototype scaffold
- Build: explore, prototype, collect evidence
- Prove: prototype runs (if applicable) + doc covers the question
- Worklog: same discipline — track what you tried and what you learned
- Adapt: checkpoint with Owner to present findings and get a decision

**After the spike:**

- If the Owner decides to proceed: the spike doc becomes a reference, and a new (or amended) SEED scopes the real work.
- If the Owner decides not to proceed: close the spike cleanly. Lessons learned go in `## Lessons`. The spike doc stays as reference or is deleted.

**What to record:**

```md
## Vision

Determine whether <X> is feasible and recommend an approach.
Deliver a working prototype and a written recommendation in docs/spike-<topic>.md.
```

---

## 11) CI integration

**Situation:** The project uses CI (GitHub Actions, GitLab CI, etc.) and you want proof to run automatically.

**Problem:** The playbook talks about proof in terms of local commands and manual runs. CI adds automation but also adds complexity (flaky runs, environment differences, external dependency on CI service).

**Pattern — CI as proof amplifier, not replacement:**

- **Proof must always be runnable locally.** CI is a convenience, not the only way to verify. If CI is down, agents can still run proof (per §4, "when proof cannot run").
- **CI config is a project file** and follows normal guardrails (tracked in git, referenced in `README.md`).
- **Record CI results in `WORKLOG.md`** with the format from §3.1: workflow name + run ID/link + pass/fail.
- **Flaky tests are `[risk]` open questions.** A test that sometimes fails for environmental reasons must be fixed or flagged, not ignored.

**Typical CI setup:**

```md
## How to prove it works

### Locally

- `npm test`

### CI

- GitHub Actions: `.github/workflows/test.yml`
- Triggers on push to `main` and on pull requests
- Runs the same `npm test` command
```

**CI-only proof (escape hatch):** Some proof can only run in CI (e.g., multi-platform matrix, deployment smoke tests). This is acceptable if:

- Documented in `README.md` as CI-only
- Local proof covers the core behavior
- CI-only proof covers platform/environment variations

**What to record:**

```md
### Process knobs

- Knob: CI provider
  - Setting: GitHub Actions
  - Why: repo is on GitHub; free tier sufficient
  - Since: YYYY-MM-DD
```

---

## 12) Multiple Owners or stakeholders

**Situation:** More than one human has authority or input over the project. A product manager, a tech lead, and a designer all have opinions.

**Problem:** The SEED Method assumes a **Single Owner**. Principle #6: "Owner decides, agents execute." Multiple decision-makers create ambiguity about who has final say.

**Pattern — Designate one Owner, formalize input channels:**

The SEED Method requires exactly one Owner. This doesn't mean only one person has input — it means one person has **final authority** for agent-facing decisions.

- **The Owner** is the person who answers SEED questions, approves scope changes, and signs off on releases.
- **Other stakeholders** provide input _through_ the Owner or through an agreed channel (e.g., issue comments, design reviews).
- **The agent always defers to the Owner** when stakeholder input conflicts.

If stakeholders want direct agent interaction, use `## Participants` to make delegation explicit:

```md
## Participants

| Role           | Name/Handle   | Platform                 | Notes                                 |
| -------------- | ------------- | ------------------------ | ------------------------------------- |
| Owner          | jveres        | —                        | Final authority on all decisions      |
| Delegate: UX   | mchen         | —                        | Authority over UI/UX decisions        |
| Delegate: API  | kpatel        | —                        | Authority over API contract decisions |
| Agent: builder | (per session) | Cursor · Claude Sonnet 4 | Primary implementation                |
```

The delegation is scoped. The Owner retains authority over everything not explicitly delegated.

**What to record:** The `## Participants` table in `SEED.md` is the record. No additional process knob needed.

---

## 13) WORKLOG is getting unwieldy

**Situation:** The worklog has grown large. Snapshot sections are verbose. Scrolling past tasks and decisions to find the log is tedious.

**Problem:** The worklog is supposed to be a dashboard — glanceable. When it's too long, it fails that purpose.

**Pattern — Aggressive pruning + archiving:**

1. **Archive early.** The playbook says archive at ~10 log entries. If it feels long at 7, archive at 7.

2. **Prune resolved open questions.** The resolution lives in its destination (Decisions, Lessons, Tasks). The open questions section should only show _actually open_ items.

3. **Collapse completed tasks.** Move completed tasks to a `### Completed` subsection at the bottom of `## Tasks`, or just remove them if they're captured in log entries. Keep only active and upcoming tasks prominent.

4. **Thin out decisions.** Carry only decisions that affect _current and future_ work. Release-specific decisions belong in the release record.

5. **Reference instead of inline.** If proof steps are long, `## Proof` says "See README.md" with only environment notes. If the task list is tracked externally, `## Tasks` is a thin index with links.

6. **Check the skeleton.** Compare your `WORKLOG.md` against the skeleton in Appendix D. If any section has grown far beyond the skeleton's implied size, it's a candidate for pruning.

7. **Leverage the dashboard cluster.** Since v3.5, the first four sections (Goal, Status, Next actions, Open questions) are designed as a one-screenful dashboard. If those four sections alone exceed one screen, they need aggressive pruning — long open-question lists, verbose status descriptions, and over-detailed next actions are the usual culprits.

**Rule of thumb:** The dashboard cluster should fit on ~1 screen. The full snapshot sections should fit on ~2–3 screens. If they don't, something needs to be archived, moved, or summarized.

**What to record:** Nothing. This is standard maintenance per the existing playbook.

---

## 14) Ambiguous or evolving SEED

**Situation:** The Owner gives a vague vision ("build something cool with this data") or the vision is deliberately exploratory and expected to evolve.

**Problem:** The SEED Method is SEED-gated. A vague SEED makes it hard to define tasks, success criteria, and proof.

**Pattern — Iterative SEED refinement:**

1. **Write the SEED as-is**, including the vagueness. Don't invent precision the Owner didn't provide.

2. **Add explicit open questions:**

   ```md
   ## Open questions (for Owner)

   - What "something cool" means — dashboard? report? interactive tool?
   - Who is the audience?
   - What counts as done?
   ```

3. **Use the first chunk as a forcing function.** Build the smallest possible thing that makes the ambiguity concrete. A rough prototype or mockup turns "something cool" into "do you mean like this?" — which is far easier for the Owner to react to.

4. **Checkpoint early and often.** With ambiguous SEED, the Adapt phase is where real direction emerges. Don't build three chunks before checking in.

5. **Amend the SEED as clarity emerges.** Each checkpoint that produces a "yes, more like that" or "no, not that" is a SEED amendment. Record it.

**Anti-pattern:** Don't wait for a perfect SEED. A vague SEED with fast iteration beats no SEED with analysis paralysis.

**What to record:** The SEED itself captures the current state of clarity. Open questions in `SEED.md` or `WORKLOG.md` capture what's still unclear.

---

## 15) Agent-to-agent handoff (relay pattern)

**Situation:** One agent finishes a session and a different agent will continue the work. Not parallel (§9) — sequential, like a relay race.

**Problem:** The incoming agent has no context beyond what's written down. Chat history may not transfer. The handoff must be self-contained.

**Important:** Agent names are session-scoped and will likely change between sessions (see recipe #17). The handoff's traceability comes from the role label, the date, and the worklog — not from the agent's session name.

**Pattern — Clean baton pass:**

The outgoing agent's final action in every session is:

1. **Update `WORKLOG.md` snapshot sections** — all of them, not just status.
2. **Write a log entry** that includes:
   - what was accomplished
   - what proof was run (with results)
   - what's next (specific, actionable)
   - any gotchas or context the next agent needs
3. **Ensure proof passes.** The incoming agent's first action will be to run proof. If it fails, the handoff was dirty.
4. **Commit/save everything.** No uncommitted work, no "I was in the middle of..." states.

The incoming agent's first actions:

1. Read `SEED.md`, `WORKLOG.md` dashboard cluster (top four sections), `README.md` (see recipe #6).
2. Check `## Participants` for your role label.
3. Run proof.
4. Read the most recent log entry for immediate context.
5. Continue from `## Next actions`.

**Quality test for a handoff:** If the incoming agent can start productive work within 5 minutes of reading the artifacts, the handoff was good. If they have to spend 30 minutes piecing together what happened, it wasn't.

**What to record:** Nothing special. This is just SEED Method discipline applied consistently. The worklog _is_ the handoff artifact — that's its purpose.

---

## 16) Partial adoption (introducing the SEED Method gradually)

**Situation:** A team or individual wants to try the SEED Method but isn't ready to go all-in. Maybe there's an existing workflow, or skepticism about the overhead.

**Problem:** The SEED Method is designed as a complete system. Cherry-picking pieces risks missing the synergies (e.g., proof without a worklog means no record; a worklog without SEED means no direction).

**Pattern — Adopt in layers:**

**Layer 1 — SEED + WORKLOG (minimum viable):**

- Write a `SEED.md` for your project.
- Keep a `WORKLOG.md` with at least: status, tasks, next actions, and a log.
- Skip everything else. No formal proof, no guardrails, no release ceremony.
- _Value:_ direction clarity + continuity across sessions.

**Layer 2 — Add proof:**

- Define "how to prove it works" in `README.md`.
- Run proof before committing. Record results.
- _Value:_ catches regressions, builds confidence.

**Layer 3 — Add guardrails + checkpoints:**

- Activate default guardrails (§11).
- Add project-specific guardrails as lessons emerge.
- Do checkpoint reviews with the Owner at natural boundaries.
- _Value:_ institutional memory, mistake prevention.

**Layer 4 — Full SEED Method:**

- Release ceremony (§10/10a).
- Multi-agent coordination (§9) if applicable.
- Audits (§7) at key milestones.
- Full learning system: lessons + practices with promotion paths.
- _Value:_ complete lifecycle management.

Each layer is independently valuable. You can stop at any layer and still benefit. But each subsequent layer amplifies the ones below it.

**What to record:**

```md
### Process knobs

- Knob: SEED Method adoption level
  - Setting: Layer 2 (SEED + WORKLOG + proof)
  - Why: gradual adoption; adding guardrails once team is comfortable
  - Since: YYYY-MM-DD
```

---

## 17) Named participants and identity

**Situation:** Multiple humans and agents are involved in a project. You need to trace who did what, who approved what, who is responsible for what — and for agents, what platform was used.

**Problem:** Owner names (like `jveres`) are stable — they persist across the entire project. Agent names (like `StarNova`, `EagleEye`) are **session-scoped** — they change on session renewal. A project might see five different agent names that all represent the same role being continued across sessions. Beyond names, agents have platform metadata (orchestrator, model) that affects capability and behavior — useful for debugging, attribution, and reproducibility.

**Pattern — Stable roles, ephemeral names, recorded platform; context-dependent usage:**

The `## Participants` table in `SEED.md` is the identity register. It maps stable roles to stable humans, marks agent names as transient, and records each agent's typical platform:

```md
## Participants

| Role            | Name/Handle   | Platform                      | Notes                     |
| --------------- | ------------- | ----------------------------- | ------------------------- |
| Owner           | jveres        | —                             |                           |
| Agent: builder  | (per session) | Claude Code · Claude Sonnet 4 | Primary implementation    |
| Agent: reviewer | (per session) | Cursor · Claude Sonnet 4      | Audit, proof verification |
```

**Platform metadata stability:**

| Metadata                                                         | Stability                      | Where it lives                                                     |
| ---------------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------ |
| **Orchestrator** (Cursor, Claude Code, Windsurf, custom harness) | Usually stable across sessions | `## Participants` Platform column                                  |
| **Model** (Claude Sonnet 4, GPT-4o, etc.)                        | Can change per session         | Default in `## Participants`; actual in log entries when different |
| **Agent name** (StarNova, CosmicRay)                             | Changes every session          | Log entries / handoff notes only                                   |

**Why platform metadata matters:**

- **Debugging:** if a chunk introduced a subtle issue, knowing the model/orchestrator helps diagnose whether it was a capability gap vs. a process gap.
- **Lessons attribution:** "this approach failed" hits differently when you know the model — a future agent on a different model might not have the same limitation.
- **Reproducibility:** if a session went exceptionally well or poorly, the setup context is part of understanding why.
- **Owner awareness:** the Owner should know what's building their project.

**Platform convention:** Use `orchestrator · model` as the format. In the Participants table, record the typical/default. In log entries and handoff notes, note the actual when it differs:

```md
### 2025-06-15 — Auth middleware added (builder / StarNova · Claude Opus 4)
```

If the platform matches the Participants table default, it can be omitted from the log entry header:

```md
### 2025-06-17 — Auth tests added (builder / CosmicRay)
```

**When to use role labels vs. names** (per Global rule #8):

- **Role labels** in procedural and authority contexts — playbook rules, guardrail attribution, SEED structure, escalation references. "Owner" signals authority; the name doesn't.
- **Participant names** in operational artifacts — log entries, commits, checkpoint messages, proposals, task discussions. Names provide traceability and human readability.

**Owner names appear directly** in operational artifacts:

```md
**Feedback from jveres**

- Approved, ship it
```

**Edge cases:**

- **Model changes mid-session** (rare but possible with some orchestrators): note it in the log entry.
- **Unknown model** (some orchestrators don't expose it): record what you know; `Cursor · unknown model` is better than nothing.
- **Custom/fine-tuned models:** use whatever identifier the orchestrator provides.
- **Non-AI agents** (human contractors acting in an agent role): Platform column is `—` (same as Owner); the role and name carry the traceability.

**Rules of thumb:**

- Use owner names and role labels for anything that needs cross-session traceability (decisions, approvals, task ownership, escalations).
- Use agent session names only as supplementary context alongside the role label.
- Record platform in the Participants table at project start; update if the default changes.
- In procedural contexts (guardrails, SEED structure, escalation rules), role labels carry authority that names don't — keep them.
- Be consistent within a project — don't switch between labeling conventions mid-stream.
- In single-agent projects with a stable Owner, the participants table is two rows. Don't overthink it.

**What to record:** The `## Participants` table in `SEED.md` (with the Platform column) is the primary record. The playbook's Global rule #8 (Identity) covers the behavioral norm. Per-session platform details go in log entries and handoff notes when they differ from the table default.

---

## 18) Collecting and promoting best practices

**Situation:** Your project (or team) is accumulating knowledge about what works well, but that knowledge lives only in individual agents' experience or scattered log entries. New agents or new projects start from scratch.

**Problem:** The SEED Method has always captured what went wrong (`## Lessons` → guardrails). But what went _right_ had no systematic collection or promotion path. Effective patterns were invisible — discovered, used once, then forgotten when the session ended.

**Pattern — Two-sided learning with promotion paths:**

The complete learning system has two sides:

```
Negative:  Mistake  → Lesson   → Guardrail  (project-enforced, prevents recurrence)
Positive:  Success  → Practice → Skill      (cross-project portable, enables reuse)
```

**Collection (automatic, every chunk):**

The §3.1 DoD requires recording practices alongside lessons. At the end of every chunk, ask two questions:

- "What went wrong or was harder than expected?" → `## Lessons`
- "What went well or was more effective than expected?" → `## Practices`

Both are append-only sections in `WORKLOG.md`. Both survive across releases. Both have archive triggers at ~15 entries.

**What makes a good practice entry:**

Good:

- "Splitting auth into middleware + validator kept both independently testable — faster iteration on auth changes."
- "Writing the API contract as a scratch doc before implementation eliminated all back-and-forth during build."
- "Running proof after every 2-3 file changes (not just per chunk) caught regressions 10x faster."

Too vague:

- "Good architecture helped." (What architecture? Helped how?)
- "Testing was useful." (What kind? What did it catch?)

The test: could a new agent read this line and _do something differently_ because of it?

**Promotion (deliberate, at checkpoints):**

Not every practice needs promotion. Most are project-specific and stay in `## Practices`. Promotion to a skill (§11a) is for patterns that:

- proved effective across multiple chunks or contexts
- are generalizable beyond the current project
- can be explained in 1–2 lines clearly enough to apply without extra context

The agent proposes promotion at a checkpoint (§6). The Owner approves. The practice moves to the project's skill file or an organizational skill library.

**Cross-project portability:**

This is where the skill format shines. Practices promoted to a skill file become available to every agent on every project that installs that skill. The knowledge survives beyond any single project:

```
Project A: discovers "contract-first API design" practice
           ↓ promoted to skill
Project B: new agent reads skill → applies pattern from day one
           ↓ discovers refinement
           ↓ practice updated
Project C: gets the refined version automatically
```

**Relationship to other mechanisms:**

| What you captured    | Where it lives | Promotion destination         |
| -------------------- | -------------- | ----------------------------- |
| Mistake / gotcha     | `## Lessons`   | `## Guardrails` (enforced)    |
| Process preference   | `## Decisions` | `### Process knobs` (default) |
| Effective pattern    | `## Practices` | Skill file (portable)         |
| Architectural choice | `## Decisions` | Stays in decisions            |

**Even failed chunks produce practices.** A chunk that fails overall may still contain approaches that worked well before the failure. §3.2 explicitly checks for this — don't throw out the good with the bad.

**What to record:**

Nothing special needed in `SEED.md`. The `## Practices` section in `WORKLOG.md` and the promotion path in §11a handle everything. If you want to track practice promotion cadence:

```md
### Process knobs

- Knob: Practice review cadence
  - Setting: every checkpoint (or every N chunks)
  - Why: ensure effective patterns are captured before session knowledge is lost
  - Since: YYYY-MM-DD
```

---

## 19) High-velocity projects (multiple releases per day)

**Situation:** The project ships frequently — multiple releases in a single day. Agents rotate rapidly. The pace is measured in hours, not days.

**Problem:** SEED Method ceremony designed for daily/weekly cadence creates friction at high velocity. Archive thresholds trigger constantly. Full log entries feel repetitive for housekeeping chunks. Audits consume a disproportionate share of available time.

**Pattern — Proportional ceremony at speed:**

The core method stays the same. Adjust the dials:

1. **Raise archive thresholds.** At 2–3 releases/day, the default ~10 log entries / ~15 lessons triggers archiving every few days. Raise to ~20 log entries / ~25 lessons if the files remain navigable. The goal is a glanceable dashboard — if it still fits on ~2 screens, the threshold is fine.

2. **Use lightweight log entries** for non-behavioral chunks (see §5). Reserve the full template for chunks that alter observable output. At high velocity, a significant fraction of chunks are doc-only or housekeeping — the lightweight format cuts log-writing time without losing traceability.

3. **Batch audit findings.** Run audits at the same cadence (milestones, pre-release), but apply housekeeping-safe fixes immediately during the audit (per §7). This eliminates the "audit then fix-pass" double-session pattern for trivial findings like stale counts and missing references.

4. **Automate derived data early.** At high velocity, hand-maintained counts and statistics drift after every session. Guardrail #9 (derived data computed, not hand-maintained) is especially critical — invest in the script or build step early. A 30-minute setup saves hours of stale-count audit findings over 10 releases.

5. **Keep SEED stable.** High velocity in releases doesn't mean high velocity in scope changes. If SEED is stable (zero amendments across many releases is achievable), that stability is a _feature_ — it means all the velocity is refinement within scope, not thrashing.

6. **Release closeout stays full.** Don't cut corners on §10a — the sealed release record and clean WORKLOG reset are what prevent accumulated cruft at high velocity. If anything, they matter _more_ when releases are frequent.

**Decision guide — when is velocity "high"?**

| Signal                                   | Adjust?                                                |
| ---------------------------------------- | ------------------------------------------------------ |
| >1 release per day sustained             | Yes                                                    |
| >5 agent sessions per day                | Yes                                                    |
| Archive triggers firing every 1–2 days   | Yes — raise thresholds                                 |
| Log entries feeling repetitive/formulaic | Yes — use lightweight format for non-behavioral chunks |
| Audits consuming >25% of a session       | Yes — batch + immediate housekeeping-safe fixes        |

**What to record:**

```md
### Process knobs

- Knob: High-velocity adjustments
  - Setting: ON — archive at ~20/~25, lightweight log for housekeeping, immediate audit doc-fixes
  - Why: multiple releases per day; default ceremony cadence creates friction
  - Since: YYYY-MM-DD
```

---

## General principles across all recipes

A few themes recur:

1. **Record your adaptations in `SEED.md` → `### Process knobs`.** This is the universal mechanism. Any time you deviate from SEED Method defaults, write it down so every agent knows.

2. **Ceremony is proportional to risk.** A weekend hack needs less than a production system. But the _minimum_ (SEED, WORKLOG, proof, guardrails) protects even small projects from common failures: forgetting what you were doing, breaking things silently, committing secrets.

3. **The artifacts serve the workflow, not the other way around.** If an artifact isn't providing value, it's either too heavy for the context (scale it down) or not being maintained (fix the habit). The answer is never "skip the artifact entirely" — it's "make it proportional."

4. **When in doubt, ask the Owner.** Every recipe above ends with recording a decision. That decision is the Owner's to make. The cookbook provides patterns; the Owner picks the one that fits.
