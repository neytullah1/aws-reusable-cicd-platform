package platform.release
import rego.v1
default allow := false
allow if {
  input.schema_version == 1
  input.environment in {"dev", "stage", "prod"}
  input.runtime in {"eks", "ecs", "lambda"}
  startswith(input.artifact.digest, "sha256:")
  input.provenance.verified == true
  input.approvals.verified == true
  input.security_checks.verified == true
}
