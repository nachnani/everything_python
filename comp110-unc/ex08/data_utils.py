"""Dictionary related utility functions."""

__author__ = "730573785"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a `list` of rows, each row represented as `dict[str, str]`."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single `column` whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform_ a table represented as a list of rows into one represented as a dictionary of columns."""

    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for column in first_row:
        result[column] = column_values(table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column_name in table:
        result[column_name] = table[column_name][0:n]
    return result


def select(col_base: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column_head in name:
        result[column_head] = col_base[column_head]
    return result


def concat(data_set_one: dict[str, list[str]], data_set_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for i in data_set_one:
        result[i] = data_set_one[i]
    for i in data_set_two:
        if i in result:
            result[i] += data_set_two[i]
        else:
            result[i] = data_set_two[i]
    return result


def count(lit: list[str]) -> dict[str, int]:
    """Produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for i in lit:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result