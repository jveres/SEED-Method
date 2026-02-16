## 7) Playbook audit (optional, trigger-based)

The Owner (or a Reviewer agent) may request a "SEED Method audit" at any time. Recommended triggers:

- after Bootstrap
- before a major polish/bundle
- before declaring "done" / release
- when confusion arises about scope, proof, or handover quality

### Audit protocol

1. Read `AGENTS.md` (this document) as source of truth.
2. Inspect repo artifacts (at minimum: `SEED.md`, `WORKLOG.md`, `README.md`, deliverables, proof artifacts).
3. **Phase compliance** — report PASS / PARTIAL / FAIL for each phase:
   - SEED
   - Bootstrap
   - Build
   - Prove
   - Worklog
   - Adapt
4. **State clarity** — report CLEAR / UNCLEAR for each question:
   - **What's done?** Can you tell from `## Status` exactly what's been completed?
   - **What's next?** Do `## Next actions` (immediately below Status) reflect actual next steps, not stale leftovers?
   - **What's blocked?** Are all blockers visible in `## Open questions` with current statuses?
   - **What's in progress?** Is it obvious from the dashboard cluster what's actively being worked on right now, or that nothing is?
   - **What does the Owner need to do?** Is it clear whether the Owner needs to act (feedback, decision, approval) or whether agents can proceed autonomously?
5. **Guardrail compliance** — report PASS / VIOLATION for each guardrail:
   - Check every default guardrail (§11).
   - Check every project-specific guardrail (`SEED.md` → `## Guardrails`).
   - For each violation: state the guardrail, the evidence, and proposed fix.
6. **Learning system health** — report HEALTHY / STALE / GAPS for:
   - **Lessons:** are they being captured? Are any stale or redundant? Any candidates for guardrail promotion?
   - **Practices:** are they being captured? Are any stale or redundant? Any candidates for skill promotion?
7. Provide concrete evidence (file names + headings/bullets) for each finding.
8. List deviations and propose minimal fixes.

### Audit constraint

- **Housekeeping-safe fixes** (per §5a edit categories) discovered during the audit may be applied immediately. Record each fix inline with the relevant finding.
- **Behavioral fixes** must not be implemented during the audit. List them as proposed fixes and ask the Owner whether to apply them.

---
