class Trainee:
    """
    Represents a trainee with a name, course, and skill points.
    """

    def __init__(self, name: str, course: str, skill_points: int = 14) -> None:
        """
        Initializes a Trainee object with a name, course, and skill points.
        :param name: The name of the trainee.
        :param course: The course the trainee is taking.
        :param skill_points: The number of skill points the trainee has (default is 14).
        """
        self.name = name
        self.course = course
        self.skill_points = skill_points

    def __str__(self) -> str:
        """
        Returns a string representation of the Trainee object.
        :return: A string containing the trainee's name, course, and skill points.
        """
        return f"Name: {self.name}\nKurs: {self.course}\nSkill: {self.skill_points}"

    def add_skill_points(self, quantity: int) -> int:
        """
        Increases the trainee's skill points by the given quantity.
        :param quantity: The number of skill points to add.
        :return: The new total number of skill points.
        """
        self.skill_points += quantity
        return self.skill_points

    def __del__(self) -> None:
        """
        Destroys the Trainee object.
        """
        pass
