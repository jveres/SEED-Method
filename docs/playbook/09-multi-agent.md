## 9) Multi-agent coordination (parallel execution contract)

When more than one agent is active, apply this section in addition to all global rules.

### External coordination tools (source of truth)

When an external coordination mechanism is in use (e.g., pi-messenger, OpenClawn), **it is the source of truth** for task claiming, file reservation, and agent communication. Do not duplicate coordination state in `WORKLOG.md` — reference the external system instead. The principles below (single ownership, escalation order, integration gate) still apply regardless of mechanism.

`WORKLOG.md` `## Tasks` remains required, but may be a thin index (task titles + external IDs/links). Ownership, claiming, and detailed status live in the external tool. The `## Coordination` line in `WORKLOG.md` snapshot sections must identify the tool and provide a link or location so the Owner can find the live state.

When no external tool is available: track ownership, reservations, and handoffs in `WORKLOG.md`. If git is also unavailable, treat `WORKLOG.md` task state + working set as the source of truth for branch-equivalent isolation and integration.

### 9.1 Task claiming and ownership

- Every active task has exactly one **owner agent** (identified by role label, not session name).
- Before implementation, owner claims task via the active coordination mechanism (external tool or `WORKLOG.md` `## Tasks`) with:
  - task id/title
  - owner (role label)
  - expected files/modules
- Only owner may close the task; reassignment must be recorded in `## Decisions`.

### 9.1a Shared artifact ownership

Unless explicitly delegated, the **driver/coordinator agent** owns updates to `WORKLOG.md`. Contributing agents report completion deltas through the active coordination mechanism (message, PR, handoff note — see §9.8). The coordinator integrates handoff notes into `WORKLOG.md` before merge/close and before Owner checkpoint messages. This prevents duplicate edits and race conditions on the shared file.

### 9.2 File/module reservation

- Reserve high-conflict paths before edits (module/feature folder preferred over single files when appropriate).
- If reservation overlaps:
  - earlier reservation has priority,
  - later agent either waits or negotiates scope split,
  - unresolved overlap is escalated (see 9.5).
- Keep reservations short-lived; release immediately after merge/handoff.

### 9.3 Branching and merge policy

Default: **trunk-based with short-lived task branches**.

- Branch naming: `task/<id>-<slug>` (or Owner-approved equivalent)
- Rebase/merge main frequently (at least daily for active branches)
- Prefer squash merge unless project policy requires otherwise
- No direct merge to main without passing integration gate (9.7)

### 9.4 Parallel work boundaries

- Prefer parallelization by independent modules/interfaces.
- For shared interfaces, agree contract first and record in `## Decisions`.
- If contract changes, notify affected task owners immediately and update plan/tasks.

### 9.5 Conflict resolution and decision escalation

Resolve in this order:

1. task owners attempt local resolution and document outcome,
2. if unresolved, coordinator/reviewer agent proposes minimal decision,
3. if still unresolved or user-facing/security/scope-impacting, escalate to Owner.

Escalate immediately for:

- SEED constraint conflicts
- irreversible architecture choices with broad impact
- security/privacy/network/persistence uncertainty
- scope changes beyond Vision

### 9.6 Parallel test/proof runs (non-interference rule)

Do not run tests or proof commands concurrently unless the project explicitly supports parallel test execution (e.g., isolated containers, per-agent ports, non-overlapping resources). If unsure, coordinate test runs sequentially:

- announce intent before running proof,
- wait for any in-progress proof run to complete,
- record your run only after exclusive access is confirmed.

If the proof slot is blocked beyond a reasonable wait window, escalate per §9.5.

### 9.7 Integration gate (required before merge/task close)

A task may be merged/closed only when:

- task acceptance criteria are met,
- required proof passes for changed behavior,
- branch is up to date with target branch (or equivalent integration baseline is confirmed by the active coordination mechanism when git/branches are unavailable),
- no unresolved reservation conflicts remain,
- `WORKLOG.md` is fresh and reflects the latest state/results.

Record gate result in the active coordination record and `WORKLOG.md`.

### 9.8 Handoff note template

Contributing agents (non-coordinator) use this template when reporting completed work via the coordination mechanism.

```md
### Handoff note — YYYY-MM-DD — <role> / <session name> · <model> — Task <N>

- Scope worked:
- Files touched:
- Behavior change summary:
- Proof run (commands + observed result):
- Open questions / blockers:
- Suggested next step:
```

Handoff notes are transient. The coordinator's integration into `WORKLOG.md` (snapshot sections + log entry) is the durable record. Handoff notes do not need to be individually referenced after integration.

---
