class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses = []  # List to store Course objects

    def assign_course(self, course):
        self.assigned_courses.append(course)

    def update_teacher_info(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def display_teacher_info(self):
        print("Teacher ID:", self.teacher_id)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)

    def get_assigned_courses(self):
        return self.assigned_courses

    def get_course_count(self):
        return len(self.assigned_courses)
