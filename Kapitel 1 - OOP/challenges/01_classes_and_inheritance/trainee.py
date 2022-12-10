class Trainee:
    """
    Diese Klasse repräsentiert eine Schüler*in mit Namen, Kurs und Fähigkeiten
    """

    def __init__(self, name: str, course: str, skill_points=14):
        print("Initialisiere Trainee")
        self.name = name
        self.course = course
        self.skill_points = skill_points

    def who_am_i(self) -> str:
        """
        Beschreibt den Trainee in einem String
        :return: Gibt einen String aus, welcher name, course und skill_level beinhaltet
        """
        return f'Name: {self.name}\nKurs: {self.course}\nSkill: {str(self.skill_points)}'

    def add_skill_points(self, quantity: int) -> int:
        """
        Erhöht den Skill des Trainees um quantity
        :param quantity: Anzahl der hinzuzufügenden Skillpunkte
        :return: Gibt den neuen Wert an Skillpunkten zurück
        """
        self.skill_points += quantity
        return self.skill_points

    def __del__(self):
        print("Objekt wird zerstört")
