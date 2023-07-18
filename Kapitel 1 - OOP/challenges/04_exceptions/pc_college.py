from no_such_course_exception import NoSuchCourseException

class PcCollege:
    """
    This class contains the courses currently offered.
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
        Adds a participant to a course if the course is found.
        Otherwise, raises a NoSuchCourseException.
        :param course_name: str, name of the course to book
        :return: bool, True if the course is found and the participant is added, False otherwise
        """
        if course_name not in self.courses:
            raise NoSuchCourseException(course_name=course_name)

        return True
