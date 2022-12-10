from no_such_course_exception import NoSuchCourseException

class PcCollege:
    """
    Diese Klasse beinhaltet unter anderem die Kurse die zurzeit angeboten werden.
    """

    def __init__(self):
        self.courses = [
            'LaTeX - Einführung',
            'Microsoft Teams - Grundlagen Seminar',
            'Python - Einführung für Programmierer',
            'MySQL - SQL Grundlagen'
        ]

    def book_course(self, course_name: str) -> bool:
        """
        Fügt einem Kurs einen Teilnehmer hinzu, sofern der Kurs gefunden wird.
        Wird andernfalls eine Exception
        :param course_name:
        :return:
        """
        if course_name not in self.courses:
            raise NoSuchCourseException(course_name=course_name)

        return True
