class Trainee:
    """
    A class representing a trainee.

    Attributes:
    -----------
    course : str
        The course the trainee is enrolled in.
    name : str
        The name of the trainee.
    skill_level : int
        The skill level of the trainee.

    Methods:
    --------
    __init__(self, name: str, course: str, skill_level: int = 0) -> None
        Initializes the Trainee object with the given name, course and skill level.
    who_am_i(self) -> str
        Returns a string containing the name, course and skill level of the trainee.
    add_skill_points(self, quantity: int) -> None
        Adds the given quantity of skill points to the trainee's skill level.
    __del__(self) -> None
        Prints a message indicating that the object has been destroyed.
    """
    def __init__(self, name: str, course: str, skill_level: int = 0) -> None:
        self.course = course
        self.name = name
        self.skill_level = skill_level

    def who_am_i(self) -> str:
        return f"My name is {self.name}, I am enrolled in {self.course} and my skill level is {self.skill_level}."

    def add_skill_points(self, quantity: int) -> None:
        self.skill_level += quantity

    def __del__(self) -> None:
        print(f"The Trainee object {self.name} has been destroyed.")


class Trainer(Trainee):
    """
    A class representing a trainer.

    Attributes:
    -----------
    course : str
        The course the trainer is teaching.
    name : str
        The name of the trainer.
    skill_level : int
        The skill level of the trainer.

    Methods:
    --------
    teach(self) -> None
        Adds 3 skill points to the trainer's skill level and prints a message indicating the course name.
        If the trainer is teaching a Java course, prints "I don't want to do this."
    """
    def teach(self) -> None:
        self.skill_level += 3
        if self.course == "Java":
            print("I don't want to do this.")
        else:
            print(f"Welcome to {self.course}!")


def test_trainees() -> None:
    """
    Tests the Trainee class by creating two Trainee objects, adding skill points to them and printing their information.
    """
    alice = Trainee(name="Alice", course="Python Aufbaukurs", skill_level=75)
    bob = Trainee(name="Bob", course="Data Science und Machine Learning mit Python")
    print(alice.who_am_i())
    print(bob.who_am_i())
    alice.add_skill_points(12)
    bob.add_skill_points(12)
    print(alice.who_am_i())
    print(bob.who_am_i())


def test_trainer() -> None:
    """
    Tests the Trainer class by creating a Trainer object, adding skill points to it, calling the teach method and printing its information.
    """
    alex = Trainer(name="Alex", course="Java", skill_level=44)
    print(alex.who_am_i())
    alex.teach()
    print(alex.who_am_i())


if __name__ == "__main__":
    test_trainees()
    test_trainer()
