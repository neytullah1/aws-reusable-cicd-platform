import copy, json, sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_release import validate
class TestRelease(unittest.TestCase):
    def setUp(self): self.d=json.loads((Path(__file__).resolve().parents[1]/'examples/release.json').read_text())
    def test_valid_structure(self): self.assertTrue(validate(self.d))
    def test_tag_not_digest(self):
        self.d['artifact']['digest']='latest'
        with self.assertRaises(ValueError): validate(self.d)
    def test_no_approval_requirement(self):
        self.d['approvals']['required']=False
        with self.assertRaises(ValueError): validate(self.d)
    def test_bad_environment(self):
        self.d['environment']='production-override'
        with self.assertRaises(ValueError): validate(self.d)
