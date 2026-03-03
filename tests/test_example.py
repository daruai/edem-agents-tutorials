"""Example tests."""

import pytest

from agents_tutorials import __version__


def test_version():
    """Package has a version."""
    assert __version__ == "0.1.0"
