## 2) Bootstrap phase (agents own it)

**Goal:** convert `SEED.md` into a runnable, provable project with minimal overhead.

If git is not initialized and not forbidden by Constraints, initialize it during Bootstrap.

Bootstrap deliverables (create what's needed for the SEED):

- `README.md` with minimal "how to run" + "how to prove"
- initial runnable artifact (even a skeleton)
- proof mechanism appropriate to the project (see §4)
- `WORKLOG.md` (required)
- plan + tasks (required; see below)
- initial commits (if git is available)

### Plan + tasks (required, but lightweight)

Location is inside `WORKLOG.md`:

- `## Plan` (short, sequential)
- `## Tasks` (numbered, small, verifiable; dependency annotations allowed, e.g., "blocked by Task 1")

Notes:

- If SEED implies minimalism (e.g., "single-file", "no build step"), keep ceremony proportional — but `WORKLOG.md` is always required.
- Avoid agent-framework vendor scaffolding unless the Owner explicitly requests it. Standard project tooling (e.g., `.github/`, CI configs) is fine.

---
