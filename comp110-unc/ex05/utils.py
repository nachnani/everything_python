"""Util functions."""

__author__ = "730573785"


def only_evens(list: list[int]) -> list[int]:
    """Returns Only Even Numbers."""
    x = list[0: len(list)]
    i: int = 0
    while (i < len(x)):
        if (x[i] % 2 == 0):
            i += 1
        else:
            x.pop(i)
    return (x)


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Returns Two Lists Into One List."""
    new_list_1 = list_1[0: len(list_1)]
    new_list_2 = list_2[0: len(list_2)]
    x: int
    if (len(new_list_1) == 0 and len(new_list_2) == 0):
        return ([])
    if (len(new_list_1) > 1):
        return_list = [new_list_1[0]]
        x = 1
        while (x < len(new_list_1)):
            return_list.append(new_list_1[x])
            x += 1
        x = 0
    elif (len(new_list_1) == 1):
        return_list = [new_list_1[0]]
        return return_list
    else:
        return_list = [new_list_2[0]]
        x = 1
    if (len(new_list_2) > 0):
        while (x < len(new_list_2)):
            return_list.append(new_list_2[x])
            x += 1
        return (return_list)
    else:
        return (return_list)


def sub(list: list[int], start: int, end: int) -> list[int]:
    """Substitute Function."""
    new_list = list[start:end]
    return (new_list)