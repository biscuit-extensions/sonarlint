from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.sonarlint import setup
from src.sonarlint.extension import SonarLint


class TestSonarLintExtension:
    def test_extension_setup(self, app_instance) -> None:
        setup(app_instance.api)
        ext = SonarLint(app_instance.api)
        issues = ext.scan_code("password = '123'\ntry:\n  pass\nexcept:\n  pass")
        assert len(issues) == 2
        assert issues[0]["type"] == "vulnerability"
