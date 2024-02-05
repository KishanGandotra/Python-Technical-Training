class OrdersCRUD:
    def __init__(self, connector):
        self.connector = connector

    def create_order(self, order_data):
        query = "INSERT INTO orders (customer_id, order_date, total_amount) VALUES (%s, %s, %s)"
        data = (order_data['customer_id'], order_data['order_date'], order_data['total_amount'])

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Order created successfully")
        except mysql.connector.Error as e:
            print(f"Error creating order: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def read_order(self, order_id):
        query = "SELECT * FROM orders WHERE order_id = %s"
        data = (order_id,)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor(dictionary=True)
            cursor.execute(query, data)
            order = cursor.fetchone()
            if order:
                print("Order details:")
                print(order)
            else:
                print("Order not found")
        except mysql.connector.Error as e:
            print(f"Error reading order: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def update_order(self, order_id, new_order_data):
        query = "UPDATE orders SET customer_id = %s, order_date = %s, total_amount = %s WHERE order_id = %s"
        data = (new_order_data['customer_id'], new_order_data['order_date'], new_order_data['total_amount'], order_id)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Order updated successfully")
        except mysql.connector.Error as e:
            print(f"Error updating order: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def delete_order(self, order_id):
        query = "DELETE FROM orders WHERE order_id = %s"
        data = (order_id,)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Order deleted successfully")
        except mysql.connector.Error as e:
            print(f"Error deleting order: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()
