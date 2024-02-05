import mysql.connector

class SISDatabase:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_student(self, first_name, last_name, date_of_birth, email, phone_number):
        insert_student_query = """
            INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number)
            VALUES (%s, %s, %s, %s, %s)
        """
        student_data = (first_name, last_name, date_of_birth, email, phone_number)
        try:
            self.cursor.execute(insert_student_query, student_data)
            self.connection.commit()
            print("Student record created successfully!")
            return True
        except mysql.connector.Error as e:
            print("Error creating student record:", e)
            self.connection.rollback()
            return False

    def enroll_student(self, student_id, course_ids):
        enrollments = []
        for course_id in course_ids:
            enrollments.append((student_id, course_id))

        insert_enrollment_query = """
            INSERT INTO Enrollments (student_id, course_id)
            VALUES (%s, %s)
        """
        try:
            self.cursor.executemany(insert_enrollment_query, enrollments)
            self.connection.commit()
            print("Student enrolled in courses successfully!")
            return True
        except mysql.connector.Error as e:
            print("Error enrolling student in courses:", e)
            self.connection.rollback()
            return False

    def assign_teacher_to_course(self, course_code, teacher_name):
        # Retrieve course ID based on course code
        select_course_query = "SELECT course_id FROM Courses WHERE course_code = %s"
        self.cursor.execute(select_course_query, (course_code,))
        course_id = self.cursor.fetchone()

        if course_id:
            # Retrieve teacher ID based on teacher name
            select_teacher_query = "SELECT teacher_id FROM teacher WHERE first_name = %s AND last_name = %s"
            self.cursor.execute(select_teacher_query, teacher_name)
            teacher_id = self.cursor.fetchone()

            if teacher_id:
                # Update course record with the new teacher
                update_course_query = "UPDATE Courses SET teacher_id = %s WHERE course_id = %s"
                self.cursor.execute(update_course_query, (teacher_id[0], course_id[0]))  # Extract the single values
                self.connection.commit()
                print("Teacher assigned to course successfully!")
            else:
                print("Teacher not found.")
        else:
            print("Course not found.")

    def record_payment(self, student_id, amount, payment_date):
        insert_payment_query = """
            INSERT INTO Payments (student_id, amount, payment_date)
            VALUES (%s, %s, %s)
        """
        payment_data = (student_id, amount, payment_date)
        try:
            self.cursor.execute(insert_payment_query, payment_data)
            self.connection.commit()
            print("Payment recorded successfully!")
            return True
        except mysql.connector.Error as e:
            print("Error recording payment:", e)
            self.connection.rollback()
            return False

    def generate_enrollment_report(self, course_name):
        # SQL query to retrieve enrollment information for the specified course
        select_enrollments_query = """
               SELECT Students.first_name, Students.last_name
               FROM Students
               INNER JOIN Enrollments ON Students.student_id = Enrollments.student_id
               INNER JOIN Courses ON Enrollments.course_id = Courses.course_id
               WHERE Courses.course_name = %s
           """

        try:
            # Execute the SQL query with the course name parameter
            self.cursor.execute(select_enrollments_query, (course_name,))
            enrollment_report = self.cursor.fetchall()

            # Print the enrollment report header
            print(f"Enrollment Report for--> {course_name}:\n")

            # Print each student enrolled in the specified course
            for enrollment in enrollment_report:
                print(f"student name-->{enrollment[0]} {enrollment[1]}")

        except mysql.connector.Error as err:
            print(f"Error generating enrollment report: {err}")

        # Other methods...

    def close_connection(self):
        # Close the database connection
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")

    def close_connection(self):
        self.connection.close()
