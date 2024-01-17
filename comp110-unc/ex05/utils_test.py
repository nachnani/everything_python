"""Importing Utils File."""

__author__ = "730573785"

from utils import only_evens, sub, concat


def test_only_evens():
    """Test for only even functions."""
    assert only_evens([1, 2, 3]) == [2]
    assert only_evens([1, 5, 3]) == []
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_concat():
    """Test for concat functions."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert concat([1, 2, 3], []) == [1, 2, 3]
    assert concat([], []) == []


def test_sub():
    """Test for sub Function."""
    li: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(li, 0, 5) == [1, 2, 3, 4, 5, 6]
    assert sub(li, -1, 3) == [1, 2, 3, 4]
    assert sub(li, 3, 10) == [4, 5, 6]
