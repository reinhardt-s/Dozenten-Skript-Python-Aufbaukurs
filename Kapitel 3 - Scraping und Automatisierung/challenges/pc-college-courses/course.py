from dataclasses import dataclass

@dataclass(order=True)
class Course:
    """A class representing a course offered by PC College."""
    name: str
    cost: int
    duration: int

    def cost_per_day(self) -> int:
        """Calculate the cost per day of the course."""
        return self.cost // self.duration
