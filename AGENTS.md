# Agent instructions (SEED Method repo)

Use this file as the **minimal, always-on contract** for working in this
repository. It is designed to stay compact so coding agents can ingest it
reliably.

If you need deeper process detail, read the full playbook (see
[Where to look](#where-to-look)).

## Non-negotiables

Follow these rules for every task.

- **SEED-gated:** Do not implement changes unless `SEED.md` exists and you are
  working within its Vision, Constraints, and Non-goals.
- **Worklog required:** Keep `WORKLOG.md` accurate. Update the dashboard
  sections and append a dated log entry for each meaningful work chunk.
- **Proof-first:** If you change behavior, run the relevant proof (tests,
  self-test, or a documented manual checklist) and record results.
- **Stop when blocked:** If you hit an unexpected blocker (tool failure,
  conflicting requirements, security concern), stop, write it into
  `WORKLOG.md` under **Open questions**, and ask for direction.
- **No secrets:** Do not commit credentials, tokens, or other sensitive data.

## Where to look

This repo is the source repository for **The SEED Method**. Keep one canonical
source for any fact.

Read these first for context:

- `SEED.md` (project Vision, Constraints, participants, guardrails)
- `WORKLOG.md` (status dashboard and the latest decisions)

Use these as references when needed:

- `SEED-Method.md` (kernel + index; canonical entrypoint)
- `docs/playbook/` (full playbook sections; canonical)
- `docs/playbook/12-appendix-skeletons.md` (skeleton templates)
- `SEED-Method-Cookbook.md` (examples and usage patterns)
- `CHANGELOG.md` (version history)

## Repo-specific workflow

Most work in this repo is documentation work.

- When you update the SEED Method, update the relevant file in
  `docs/playbook/` and keep `SEED-Method.md` (index) in sync.
- When you update examples or “how to apply,” update
  `SEED-Method-Cookbook.md`.
- Track version changes in `CHANGELOG.md`.
- After a version update, reload the root playbook: re-read `SEED-Method.md`
  and ensure `AGENTS.md` still points to the right canonical sources.
- **Dogfood check (guardrail):** This repo runs on the SEED Method it defines.
  After any playbook change, verify that the repo's own bootstrap artifacts
  (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`) and generated files (`dist/`,
  `skills/`) are consistent with the updated method. If the playbook adds or
  changes a rule, the repo must follow that rule itself.
- After changing any file in `docs/playbook/`, rebuild generated artifacts:
  - Rebuild the full distribution: `./scripts/build-dist.py`
  - Rebuild the kernel distribution: `./scripts/build-dist.py --variant kernel`
  - Rebuild the skills.sh skill: `./scripts/build-skill.py`
- Before release/sign-off, verify generated artifacts are up to date:
  - `./scripts/check-dist.py` (checks both dist variants)
  - `./scripts/check-skill.py`

## Output expectations

When you finish a work chunk, leave a crisp record.

- Update `WORKLOG.md` dashboard sections (Status, Next actions, Open questions).
- Append a dated entry in `WORKLOG.md` describing:
  - what changed
  - what proof ran (or why it could not run)
  - what is next
