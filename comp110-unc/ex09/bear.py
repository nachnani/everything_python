"""File to define Bear class."""


class Bear:
    """Bear functions."""
    # attributes

    age: int
    hunger_score: int

    def __init__(self):
        """The inital values for bears in the river simulation."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """One day of the river simulation for a bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Eating function for the bears."""
        if num_fish > 0:
            self.hunger_score += num_fish