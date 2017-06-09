import pytest


def test_something():
    assert True


@pytest.mark.xfail
def test_fail():
    assert False