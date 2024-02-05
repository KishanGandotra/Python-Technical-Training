class SIS:
    def __init__(self):
        self.students = []   # List to store Student objects
        self.courses = []    # List to store Course objects
        self.teachers = []   # List to store Teacher objects
        self.enrollments = [] # List to store Enrollment objects
        self.payments = []    # List to store Payment objects

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_enrollment(self, enrollment):
        self.enrollments.append(enrollment)

    def add_payment(self, payment):
        self.payments.append(payment)

    def get_enrollments_for_student(self, student):
        return [enrollment for enrollment in self.enrollments if enrollment.student == student]

    def get_courses_for_teacher(self, teacher):
        return [course for course in teacher.assigned_courses]

    def get_payments_for_student(self, student):
        return [payment for payment in self.payments if payment.student == student]

    def generate_enrollment_report(self, course):
        enrollments = [enrollment for enrollment in self.enrollments if enrollment.course == course]
        return enrollments

    def generate_payment_report(self, student):
        payments = [payment for payment in self.payments if payment.student == student]
        return payments
