"""File to define Fish class."""


class Fish:
    """Fish functions."""
    # attributes

    age: int

    def __init__(self):
        """Initial attributes."""
        self.age = 0

    def one_day(self):
        """One effects for the fish in sim."""
        self.age += 1