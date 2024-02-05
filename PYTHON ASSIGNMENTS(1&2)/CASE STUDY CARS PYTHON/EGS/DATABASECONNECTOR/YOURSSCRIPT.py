import mysql.connector
from datetime import datetime

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def search_products(self, keyword):
        try:
            query = "SELECT * FROM products WHERE productname LIKE %s OR description LIKE %s"
            self.cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
            products = self.cursor.fetchall()

            if products:
                print("Search Results:")
                for product in products:
                    print(
                        f"Product ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, Price: ${product[3]}")
            else:
                print("No products found matching the search criteria.")
        except mysql.connector.Error as err:
            print(f"Error searching products: {err}")

    def register_customer(self, firstname, email, phone, address):
        query = "INSERT INTO customers (firstname, email, phone, address) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (firstname, email, phone, address))
        self.connection.commit()
        print("Customer registered successfully.")
    


if __name__ == "__main__":
    # Example usage
    db_connector = DatabaseConnector(
        host="localhost",
        user="root",
        password="root",
        database="egs"
    )

    db_connector.register_customer("JohNYn", "johnY@example.com", "1234567890", "123 Main St")
    db_connector.search_products("smartphone")
    db_connector.close_connection()