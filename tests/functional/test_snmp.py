# SPDX-License-Identifier: Apache-2.0
import os

import testtools

from bandit.core import config
from bandit.core import manager


class SnmpModernApiTests(testtools.TestCase):
    def test_modern_api(self):
        """Recognize modern PySNMP imports without matching unrelated calls."""
        b_mgr = manager.BanditManager(config.BanditConfig(), "file")
        b_mgr.discover_files([os.path.join("examples", "snmp_modern.py")])
        b_mgr.run_tests()
        issues = b_mgr.get_issue_list()
        self.assertEqual(
            [("B508", line) for line in range(15, 22)]
            + [("B509", line) for line in range(24, 28)],
            [(issue.test_id, issue.lineno) for issue in issues],
        )
        self.assertTrue(all(issue.severity == "MEDIUM" for issue in issues))
        self.assertTrue(all(issue.confidence == "HIGH" for issue in issues))
