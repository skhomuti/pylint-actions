"""
Pylint reporter for GitHub Actions
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from pylint.reporters.text import TextReporter

if TYPE_CHECKING:
    from pylint.lint.pylinter import PyLinter


class ActionsReporter(TextReporter):
    """
    Reporter for GitHub Actions based on the TextReporter.
    """
    name = "actions"

    def __init__(self, *args, **kwargs):
        self.line_format = "::error file={path},line={line},endLine={end_line}," \
                           "title=Pylint: {msg_id} ({symbol})::{msg}"
        super().__init__(*args, **kwargs)


def register(linter: PyLinter):
    """
    Register the reporter with Pylint.
    """
    linter.register_reporter(ActionsReporter)
