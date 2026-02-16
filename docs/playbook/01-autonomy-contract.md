## 1) Autonomy contract (default)

Unless `SEED.md` restricts it, agents are authorized to:

- choose tech stack and minimal architecture
- initialize git and set up repo structure
- create/modify any files needed to deliver the Vision
- add tooling/build steps if not forbidden by Constraints
- refactor for maintainability
- run full-speed end-to-end delivery

Agents must ask the Owner before:

- violating any SEED constraint
- expanding scope beyond the Vision
- adding external dependencies when dependency policy is unclear or restrictive
- making user-facing product/design decisions that are ambiguous
- introducing security/privacy risk, network access, or data persistence when not explicitly allowed

### Security hard rule (non-negotiable)

- Never commit sensitive data (credentials, secrets), ensure they are ignored by git.

---
