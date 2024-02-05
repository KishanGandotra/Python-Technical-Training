class PaymentProcessing:
    def __init__(self, connector):
        self.connector = connector

    def process_payment(self, order_id, payment_details):
        # Assuming payment_details contains payment method, amount, etc.
        query = "INSERT INTO payments (order_id, payment_method, amount, status) VALUES (%s, %s, %s, %s)"
        data = (order_id, payment_details['payment_method'], payment_details['amount'], 'Pending')

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Payment processed successfully")
        except mysql.connector.Error as e:
            print(f"Error processing payment: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def update_payment_status(self, payment_id, new_status):
        query = "UPDATE payments SET status = %s WHERE payment_id = %s"
        data = (new_status, payment_id)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Payment status updated successfully")
        except mysql.connector.Error as e:
            print(f"Error updating payment status: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()
