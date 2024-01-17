"""File to define River class."""

__author__ = "730573785"

from fish import Fish
from bear import Bear


class River:
    """River Class for the river sim."""

    # attributes

    day: int
    bears: int
    fish: int

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages for fish and bears."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int):
        """Removes fish if needed."""
        for i in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)

    def bears_eating(self):
        """Bears eating process."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)

    def check_hunger(self):
        """Checks hunger bars for bears in the sim."""
        surviving_bears = []

        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def repopulate_fish(self):
        """Repopulation process for fish."""
        num_fish = len(self.fish)
        new_fish = num_fish // 2 * 4
        for i in range(new_fish):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """Repopulation process for bears."""
        num_bears = len(self.bears)
        new_bears = num_bears // 2
        for i in range(new_bears):
            self.bears.append(Bear())

    def view_river(self):
        """Gives description of the simulation."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates a week in the simulation."""
        for days in range(7):
            self.one_river_day()
