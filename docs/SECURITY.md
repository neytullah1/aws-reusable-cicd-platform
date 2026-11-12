# Security and bypass-resistance model

| Attack | Defense outside developer control | What remains to configure |
|---|---|---|
| Edit caller to skip scan | Organization-enforced required workflow/check + trusted deploy verifier | GitHub org rulesets and security-owned GitHub App |
| Change reusable workflow ref | Immutable audited commit pin + protected release tags + `job_workflow_ref` trust controls where supported | OIDC claim customization and exact trust tests |
| Forge passing check | Required check pinned to trusted GitHub App identity, not just a check name | GitHub ruleset and App ownership |
| Deploy directly from laptop | Account-scoped IAM/SCP + no human deploy permissions + audited break-glass | AWS Org SCP, IAM and CloudTrail |
| Swap artifact after review | Digest-only references + provenance subject verification at deployment | Registry attestation verification |
| Self-approve | Protected GitHub environment, no self-review, separate owners | Organization policy/plan verification |
| Poison AI reviewer | Redaction, data minimization, treat diff as untrusted text, no execution | Separate read-only GitHub App and model gateway |
| Alter policy bundle | Security-owned repo and immutable policy release | External policy decision service |

**Hard boundary:** GitHub environment approvals are not equivalent to AWS authorization. A malicious workflow with access to a broad AWS role could bypass GitOps; IAM must limit actions and trusted principals. ECS and Lambda need an external verification/authorization step, not a mere YAML `if` statement. GitOps for EKS requires Argo CD project restrictions, protected Git repository, signed/verified commits where required, scoped sync credentials, and admission policies.

**Plan caveat:** Availability of organization rulesets, required workflows, environment reviewers, and bypass restrictions varies by GitHub product/plan and repository visibility. Verify before claiming enforcement.

**Secrets:** no credentials, tokens, customer names, production account IDs, plan files or raw Terraform state in public repos. Use secret scanning and redact AI inputs.
