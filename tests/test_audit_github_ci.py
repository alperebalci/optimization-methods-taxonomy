"""Pure, offline unit tests for current-head CI state classification."""

import unittest

from scripts.audit_github_ci import classify_runs, render_report


def entry(sha, wid, name, status="completed", conclusion="success", number=1):
    return {"head_sha": sha, "workflow_id": wid, "name": name,
            "status": status, "conclusion": conclusion, "run_number": number, "run_attempt": 1}


class CIHealthTests(unittest.TestCase):
    def test_no_workflow_is_not_green(self):
        self.assertEqual(classify_runs("abc", []), ("uncovered", []))

    def test_historical_success_is_stale(self):
        self.assertEqual(classify_runs("abc", [entry("old", 1, "checks")]), ("stale", []))

    def test_failures_on_current_head_are_reported(self):
        status, failing = classify_runs(
            "abc", [entry("abc", 1, "unit"), entry("abc", 2, "integration", conclusion="failure")])
        self.assertEqual(status, "failure")
        self.assertEqual(failing, ["integration"])

    def test_last_rerun_overrides_old_failed_attempt(self):
        checks = [entry("abc", 1, "unit", conclusion="failure", number=2),
                  entry("abc", 1, "unit", conclusion="success", number=3)]
        self.assertEqual(classify_runs("abc", checks), ("success", []))

    def test_pending_and_cancelled_are_never_green(self):
        self.assertEqual(
            classify_runs("abc", [entry("abc", 1, "unit", status="in_progress", conclusion=None)])[0],
            "pending",
        )
        self.assertEqual(
            classify_runs("abc", [entry("abc", 1, "unit", conclusion="cancelled")])[0],
            "incomplete",
        )

    def test_report_marks_uncovered_explicitly(self):
        result = {"repo": "alice/not-tested", "status": "uncovered",
                  "url": "https://github.com/alice/not-tested/actions"}
        report = render_report("alice", [result])
        self.assertIn("uncovered: 1", report)
        self.assertIn("Private repositories are not included", report)


if __name__ == "__main__":
    unittest.main()
