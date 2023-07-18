from trainee import Trainee


class Trainer(Trainee):
    """
    Trainer class inherits from Trainee class and adds the ability to teach.
    """
    def __init__(self, name: str, course: str, skill_points: int):
        """
        Initializes Trainer object with name, course and skill points.
        """
        super().__init__(name, course, skill_points)

    def teach(self):
        """
        Adds 3 skill points to the Trainer object and prints a message based on the course.
        """
        self.add_skill_points(3)
        if self.course == 'Java':
            print('Ich möchte das nicht.')
        else:
            print(f'Willkommen zu {self.course}')
