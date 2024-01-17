"""Dictionaries Test."""

__author__ = "730573785"

from dictionary import invert, favorite_color, count
import pytest


def test_invert_empty_dict() -> None:
    """Test edge case of empty list."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_repeating_keys() -> None:
    """Test to confirm error is raised if keys repeat."""
    dictionary: dict[str, str] = {}
    with pytest.raises(KeyError):
        dictionary = {"hey": "yo", "morning": "hello", "water": "drink", "yellow": "yo"}
        invert(dictionary)


def test_normal_keys() -> None:
    """Normal Dictionary test."""
    xs: dict[str, str] = {"hey": "you", "rick": "rop", "cool": "coo", "pip": "bro"}
    assert invert(xs) == {"you": "hey", "rop": "rick", "coo": "cool", "bro": "pip"}


def test_two_modes() -> None:
    """Testing a list with multiple modes."""
    xs: list[str] = ["ye", "yo", "ye", "yo"]
    assert count(xs) == {"ye": 2, "yo": 2}


def test_empty_list() -> None:
    """Testing a normal list with no modes."""
    xs: list[str] = []
    assert count(xs) == {}


def test_normal_list() -> None:
    """Testing a normal list with no modes."""
    xs: list[str] = {"violet", "how", "green", "what"}
    assert count(xs) == {"violet": 1, "how": 1, "green": 1, "what": 1}


def test_one_mode() -> None:
    """Testing normal dict with one use."""
    xs: dict[str, str] = {"max": "violet", "sebastion": "violet", "lewis": "violet", "charles": "green"}
    assert favorite_color(xs) == "violet"


def test_no_mode() -> None:
    """Testing normal dict with no mode."""
    xs: dict[str, str] = {"rio": "grey", "lando": "yellow", "fernando": "brown", "pierre": "green"}
    assert favorite_color(xs) == "grey"


def test_empty_dict_two() -> None:
    """Testing normal dict with no mode."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""