class SalesReporting:
    def __init__(self, connector):
        self.connector = connector

    def generate_sales_report(self, start_date, end_date):
        query = "SELECT * FROM orders WHERE order_date BETWEEN %s AND %s"
        data = (start_date, end_date)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor(dictionary=True)
            cursor.execute(query, data)
            orders = cursor.fetchall()

            total_sales = sum(order['total_amount'] for order in orders)
            total_orders = len(orders)

            print(f"Total Sales: ${total_sales}")
            print(f"Total Orders: {total_orders}")

            # Additional processing or reporting logic can be added here

        except mysql.connector.Error as e:
            print(f"Error generating sales report: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()
