from SIS_DATABASE import SISDatabase

# Main code for student enrollment, teacher assignment, payment record, and enrollment report tasks
if __name__ == "__main__":
    # Initialize SISDatabase object
    db = SISDatabase(host='localhost', user='root', password='root', database='sisdb')

    # Task 8: Student Enrollment
    first_name = 'k'
    last_name = 'g'
    date_of_birth = '2000-07-15'
    email = 'kg@example.com'
    phone_number = '123-456-7890'
    if db.create_student(first_name, last_name, date_of_birth, email, phone_number):
        student_id = db.cursor.lastrowid
        course_ids = [1, 2]  # Assuming course IDs for Introduction to Programming and Mathematics 101
        db.enroll_student(student_id, course_ids)

    # Task 9: Teacher Assignment
    course_code = 'CS101'
    teacher_first_name = 'Matthew'  # Adjust the first name
    teacher_last_name = 'Anderson'  # Adjust the last name
    teacher_name = (teacher_first_name, teacher_last_name)  # Construct a tuple
    db.assign_teacher_to_course(course_code, teacher_name)

    # Task 10: Payment Record
    student_id = 7
    amount = 500.00
    payment_date = '2023-04-10'
    db.record_payment(student_id, amount, payment_date)

    # Task 11: Enrollment Report Generation
    course_name = 'Introduction to Computer Science'
    db.generate_enrollment_report(course_name)

    # Close database connection
    db.close_connection()
