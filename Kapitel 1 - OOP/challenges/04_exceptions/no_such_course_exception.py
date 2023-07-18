class NoSuchCourseException(BaseException):
    """
    Exception raised when a course does not exist.
    """
    def __init__(self, course_name):
        self.course_name = course_name
        super().__init__(f'Der Kurs "{course_name}" existiert nicht.')
