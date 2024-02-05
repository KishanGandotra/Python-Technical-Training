class Course:
    def __init__(self, course_id, course_name, course_code, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.enrollments = []  # List to store Enrollment objects

    def add_enrollment(self, enrollment):
        self.enrollments.append(enrollment)

    def update_course_info(self, course_name, course_code, instructor_name):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name

    def display_course_info(self):
        print("Course ID:", self.course_id)
        print("Course Name:", self.course_name)
        print("Course Code:", self.course_code)
        print("Instructor Name:", self.instructor_name)

    def get_enrollments(self):
        return self.enrollments

    def get_instructor_name(self):
        return self.instructor_name

    def get_student_count(self):
        return len(self.enrollments)
