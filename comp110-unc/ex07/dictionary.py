"""Dictionaries."""

__author__ = "730573785"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    if x == {}:
        return {}
    result: dict[str, str] = {}
    for int in x:
        result[x[int]] = int
    counted = count(list(x.values()))
    if max(list(counted.values())) > 1:
        raise KeyError("Values are the same")
    return result


def favorite_color(x: dict[str, str]) -> str:
    """Returns value with most occurences."""
    if x == {}:
        return ""
    results = count(x.values())
    keys = list(results.keys())
    values = list(results.values())
    index = values.index(max(values))
    return keys[index]


def count(x: list[str]) -> dict[str, int]:
    """Produces a dict where each key is a unique value in the given list."""
    result: dict[str, str] = {}
    for i in x:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result