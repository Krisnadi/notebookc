"""Tests for `notebookc` package."""
import pytest
from notebookc import notebookc


def test_convert(capsys):
    """Correct my_name argument prints"""
    notebookc.convert("Jill")
    captured = capsys.readouterr()
    assert "Jill" in captured.out
