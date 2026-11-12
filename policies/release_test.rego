package platform.release
import rego.v1
test_deny_unverified if {
  not allow with input as {"schema_version":1,"environment":"prod","runtime":"ecs","artifact":{"digest":"sha256:abc"},"provenance":{"verified":false},"approvals":{"verified":true},"security_checks":{"verified":true}}
}
