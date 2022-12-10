from trainee import Trainee


class Trainer(Trainee):
    """
    Trainer haben dieselben Fähigkeiten wie Trainees.
    Sie können jedoch zusätzlich unterrichten.
    """
    def __init__(self, name: str, course: str, skill_points: int):
        print('Initialisiere Trainer')
        super(Trainer, self).__init__(name, course, skill_points)

    def teach(self):
        """
        Fügt zuerst dem Trainer 3 Skillpunkte hinzu.
        Falls der Trainer den Kurs in Java hält, wird mit print() "Ich möchte das nicht." ausgegeben.
        Andernfalls wird "Willkommen zu 'Kursname'" ausgegeben
        """
        self.add_skill_points(3)
        if self.course == 'Java':
            print(f'Ich möchte das nicht.')
        else:
            print(f'Willkommen zu {self.course}')



