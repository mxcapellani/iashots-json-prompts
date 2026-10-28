#!/usr/bin/env python3
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from validate import ROOT, REQUIRED, validate, validate_prompt

class ContractTests(unittest.TestCase):
    def setUp(self):
        self.sample = json.loads((ROOT / "examples/studio-portrait.json").read_text())
    def test_valid(self):
        self.assertEqual(validate(), [])
        self.assertEqual(validate_prompt(json.dumps(self.sample)), [])
    def test_missing_key(self):
        del self.sample["Pose"]
        self.assertTrue(validate_prompt(json.dumps(self.sample)))
    def test_extra_key(self):
        self.sample["Other"] = "Not allowed"
        self.assertTrue(validate_prompt(json.dumps(self.sample)))
    def test_renamed_key(self):
        self.sample["Camera"] = self.sample.pop("Camera Settings")
        self.assertTrue(validate_prompt(json.dumps(self.sample)))
    def test_wrong_type(self):
        self.sample["Subject"] = []
        self.assertTrue(validate_prompt(json.dumps(self.sample)))
    def test_empty_value(self):
        self.sample["Subject"] = ""
        self.assertTrue(validate_prompt(json.dumps(self.sample)))
    def test_whitespace_value(self):
        self.sample["Subject"] = "   "
        self.assertTrue(validate_prompt(json.dumps(self.sample)))
    def test_duplicate_key(self):
        self.assertTrue(validate_prompt('{"Subject":"A","Subject":"B"}'))
    def test_trailing_comma(self):
        self.assertTrue(validate_prompt('{"Subject":"A",}'))
    def test_comments(self):
        self.assertTrue(validate_prompt('{//comment\n"Subject":"A"}'))
    def test_nan(self):
        self.assertTrue(validate_prompt('{"Subject":NaN}'))
    def test_missing_skill(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / "repo"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns("__pycache__", ".git", ".venv"))
            (root / REQUIRED[0]).unlink()
            self.assertTrue(validate(root))

if __name__ == "__main__":
    unittest.main()
