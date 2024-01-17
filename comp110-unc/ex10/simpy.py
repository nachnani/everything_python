"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730573785"


class Simpy:
    """Simpy Class."""

    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, values: list[float]):
        """Initialize attributes of new object."""
        self.values = values

    def __str__(self) -> str:
        """Will override power operator."""
        return f"Simpy({self.values})"

    def fill(self, fl: float, x: int) -> None:
        """Will override power operator."""
        i: int = 0
        result: list[float] = []
        while i < x:
            result.append(fl)
        i += 1
        self.values = result
        return self.values

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Will override power operator."""
        result: list[float] = []
        assert step != 0.0
        while abs(stop) > abs(start):
            result.append(start)
            start += step
        self.values = result
        return self.values

    def sum(self) -> float:
        """Will override power operator."""
        Sum = sum(self.values)
        return Sum

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Will override power operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Will override power operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Equal to."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Filter objects with a mask."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: list[float] = []
        for i in range(len(rhs)):
            if rhs[i]:
                result.append(self.values[i])
        return
