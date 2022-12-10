class NoSuchCourseException(BaseException):
    def __init__(self, course_name):
        self.course_name = course_name
        self.message = f'Der Kurs "{course_name}" existiert nicht.'
        super().__init__(self.message)
