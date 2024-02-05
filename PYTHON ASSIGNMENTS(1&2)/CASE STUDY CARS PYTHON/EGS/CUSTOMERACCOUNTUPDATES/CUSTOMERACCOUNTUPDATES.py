class CustomerAccountUpdates:
    def __init__(self, connector):
        self.connector = connector

    def update_customer_info(self, customer_id, new_info):
        query = "UPDATE customers SET email = %s, phone = %s, address = %s WHERE customer_id = %s"
        data = (new_info['email'], new_info['phone'], new_info['address'], customer_id)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Customer information updated successfully")
        except mysql.connector.Error as e:
            print(f"Error updating customer information: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()
