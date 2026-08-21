from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class SonarLint(Extension):
    """Scan source code for bugs, code smells, and security vulnerabilities."""

    def __init__(self, api: ExtensionsAPI) -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("SonarLint extension initialised.")

    def scan_code(self, code: str) -> list[dict]:
        findings = []
        for line_no, line in enumerate(code.splitlines(), start=1):
            if "password" in line.lower() and "=" in line:
                findings.append({"line": line_no, "type": "vulnerability", "message": "Hardcoded credentials detected."})
            if "except:" in line.replace(" ", ""):
                findings.append({"line": line_no, "type": "code_smell", "message": "Bare except clause catches all exceptions."})
        return findings

    def install(self) -> None:
        self.api.logger.info("SonarLint extension installed.")
