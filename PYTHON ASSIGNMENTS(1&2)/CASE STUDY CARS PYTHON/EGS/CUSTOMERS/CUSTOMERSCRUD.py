class CustomersCRUD:
    def __init__(self, connector):
        self.connector = connector

    def create_customer(self, customer_data):
        query = "INSERT INTO customers (first_name, last_name, email, phone, address) VALUES (%s, %s, %s, %s, %s)"
        data = (customer_data['first_name'], customer_data['last_name'], customer_data['email'], customer_data['phone'], customer_data['address'])

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Customer created successfully")
        except mysql.connector.Error as e:
            print(f"Error creating customer: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def read_customer(self, customer_id):
        query = "SELECT * FROM customers WHERE customer_id = %s"
        data = (customer_id,)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor(dictionary=True)
            cursor.execute(query, data)
            customer = cursor.fetchone()
            if customer:
                print("Customer details:")
                print(customer)
            else:
                print("Customer not found")
        except mysql.connector.Error as e:
            print(f"Error reading customer: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def update_customer(self, customer_id, new_customer_data):
        query = "UPDATE customers SET first_name = %s, last_name = %s, email = %s, phone = %s, address = %s WHERE customer_id = %s"
        data = (new_customer_data['first_name'], new_customer_data['last_name'], new_customer_data['email'], new_customer_data['phone'], new_customer_data['address'], customer_id)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Customer updated successfully")
        except mysql.connector.Error as e:
            print(f"Error updating customer: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def delete_customer(self, customer_id):
        query = "DELETE FROM customers WHERE customer_id = %s"
        data = (customer_id,)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Customer deleted successfully")
        except mysql.connector.Error as e:
            print(f"Error deleting customer: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()
