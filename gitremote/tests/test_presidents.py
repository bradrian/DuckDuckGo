import pytest

from gitremote.presidents import get_presidents


def test_get_presidents():
    assert get_presidents() == "hello"
