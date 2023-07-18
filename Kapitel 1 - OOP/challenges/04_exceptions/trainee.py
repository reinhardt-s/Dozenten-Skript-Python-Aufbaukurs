class Trainee:
    """
    This class represents a trainee with a name, course, and skill points.
    """

    def __init__(self, name: str, course: str, skill_points: int = 14) -> None:
        """
        Initializes a Trainee object with a name, course, and skill points.
        :param name: The name of the trainee.
        :param course: The course of the trainee.
        :param skill_points: The skill points of the trainee.
        """
        print(f"Initializing Trainee {name}")
        self.name = name
        self.course = course
        self.skill_points = skill_points

    def __str__(self) -> str:
        """
        Returns a string representation of the Trainee object.
        :return: A string representation of the Trainee object.
        """
        return f'Name: {self.name}\nCourse: {self.course}\nSkill Points: {self.skill_points}'

    def add_skill_points(self, quantity: int) -> int:
        """
        Increases the skill points of the trainee by the given quantity.
        :param quantity: The quantity of skill points to add.
        :return: The new skill points value.
        """
        self.skill_points += quantity
        return self.skill_points

    def __del__(self) -> None:
        """
        Destroys the Trainee object.
        """
        print(f"Destroying Trainee object {self.name}")
