class Enrollment:
    def __init__(self, enrollment_id, student, course, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student = student  # Reference to Student object
        self.course = course    # Reference to Course object
        self.enrollment_date = enrollment_date

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course

    def display_enrollment_info(self):
        print("Enrollment ID:", self.enrollment_id)
        print("Student:", self.student.first_name, self.student.last_name)
        print("Course:", self.course.course_name)
        print("Enrollment Date:", self.enrollment_date)
