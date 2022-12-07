# https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class Course:
    name: str
    cost: int
    duration: int

    def cost_per_day(self) -> int:
        return self.cost // self.duration

    def __gt__(self, other):
        if self.cost_per_day() > other.cost_per_day():
            return True

        return False

    def __lt__(self, other):
        if self.cost_per_day() < other.cost_per_day():
            return True

        return False

    def __eq__(self, other):
        if self.cost_per_day() == other.cost_per_day():
            return True

        return False
