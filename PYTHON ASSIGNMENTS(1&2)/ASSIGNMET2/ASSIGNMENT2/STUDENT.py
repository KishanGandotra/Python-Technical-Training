class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.enrollments = []  # List to store Enrollment objects
        self.payments = []  # List to store Payment objects

    def enroll_in_course(self, enrollment):
        self.enrollments.append(enrollment)

    def make_payment(self, payment):
        self.payments.append(payment)

    def update_student_info(self, first_name, last_name, date_of_birth, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number

    def display_student_info(self):
        print("Student ID:", self.student_id)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Date of Birth:", self.date_of_birth)
        print("Email:", self.email)
        print("Phone Number:", self.phone_number)

    def get_enrolled_courses(self):
        return [enrollment.course for enrollment in self.enrollments]

    def get_payment_history(self):
        return self.payments
