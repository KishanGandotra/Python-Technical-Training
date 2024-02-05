class Payment:
    def __init__(self, payment_id, student, amount, payment_date):
        self.payment_id = payment_id
        self.student = student  # Reference to Student object
        self.amount = amount
        self.payment_date = payment_date

    def get_student(self):
        return self.student

    def get_payment_amount(self):
        return self.amount

    def get_payment_date(self):
        return self.payment_date

    def display_payment_info(self):
        print("Payment ID:", self.payment_id)
        print("Student:", self.student.first_name, self.student.last_name)
        print("Amount:", self.amount)
        print("Payment Date:", self.payment_date)
