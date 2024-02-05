class OrderDetailsCRUD:
    def __init__(self, connector):
        self.connector = connector

    def create_order_detail(self, order_detail_data):
        query = "INSERT INTO order_details (order_id, product_id, quantity) VALUES (%s, %s, %s)"
        data = (order_detail_data['order_id'], order_detail_data['product_id'], order_detail_data['quantity'])

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Order detail created successfully")
        except mysql.connector.Error as e:
            print(f"Error creating order detail: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def read_order_detail(self, order_detail_id):
        query = "SELECT * FROM order_details WHERE order_detail_id = %s"
        data = (order_detail_id,)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor(dictionary=True)
            cursor.execute(query, data)
            order_detail = cursor.fetchone()
            if order_detail:
                print("Order detail:")
                print(order_detail)
            else:
                print("Order detail not found")
        except mysql.connector.Error as e:
            print(f"Error reading order detail: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def update_order_detail(self, order_detail_id, new_order_detail_data):
        query = "UPDATE order_details SET order_id = %s, product_id = %s, quantity = %s WHERE order_detail_id = %s"
        data = (new_order_detail_data['order_id'], new_order_detail_data['product_id'], new_order_detail_data['quantity'], order_detail_id)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Order detail updated successfully")
        except mysql.connector.Error as e:
            print(f"Error updating order detail: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def delete_order_detail(self, order_detail_id):
        query = "DELETE FROM order_details WHERE order_detail_id = %s"
        data = (order_detail_id,)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Order detail deleted successfully")
        except mysql.connector.Error as e:
            print(f"Error deleting order detail: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()
