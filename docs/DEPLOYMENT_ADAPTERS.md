# Deployment adapters — design contracts, not enabled deploy scripts

Common input: application, runtime, environment, Git SHA, immutable artifact URI/digest, trusted provenance identity, security policy decision, approval evidence. Only a trusted verification service can mint a short-lived deployment authorization.

* **EKS:** update a protected GitOps repository through a reviewed PR with image digest; Argo CD reconciles after merge. Cluster admission should enforce image provenance and allowed registries. Roll back via revert to previous approved digest. Do not grant cluster-admin to CI.
* **ECS:** register a new task definition pinned to ECR digest; deploy via constrained ECS service permissions, observe deployment health/alarms; roll back to previous approved task definition. Separate deploy role per account/service.
* **Lambda:** publish a version from a digest-pinned, verified artifact; shift an alias with CodeDeploy canary/linear rollout and CloudWatch alarms; roll back alias to prior version. ZIP workflows need a separate immutable S3 object/version contract; container image contract does not directly cover ZIP.

**This portfolio intentionally does not include executable production deploy steps:** the external verifier, AWS role restrictions, GitOps controller and runtime resources are not provisioned. Dispatcher has an explicit `exit 1` security hold.
