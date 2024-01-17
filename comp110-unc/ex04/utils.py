"""Utility Function Exercise."""

__author__ = "730573785"


def all(num: list[int], x: int) -> bool:
    """Determines if a list contains the same number."""
    i: int = 0
    if (len(num) == 0):
        return False

    while (i < len(num)):
        if (x != num[i]):
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Determines the max int from a list."""
    if (len(input)) == 0:
        raise ValueError("max() arg is an empty list")

    i: int = 0
    max: int = input[0]

    while (i < len(input)):
        if (input[i] > max):
            max = input[i]
        i += 1
    return (max)


def is_equal(setone: list[int], settwo: list[int]) -> bool:
    """Determines if two sets are equal to each other."""
    if setone == settwo:
        return True
    else:
        return False