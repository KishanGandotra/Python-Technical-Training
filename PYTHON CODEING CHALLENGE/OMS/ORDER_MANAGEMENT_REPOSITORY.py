import mysql.connector
from mysql.connector import Error
from IORDERMANAGEMENTREPOSITORY import IOrderManagementRepository
from USER import User
from PRODUCT import Product

class OrderManagementRepository(IOrderManagementRepository):
    def __init__(self):
        try:
            # Establish database connection
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='oms'
            )

            if self.conn.is_connected():
                print('Connected to the database')
                self.cursor = self.conn.cursor()
            else:
                print('Failed to connect to the database')

        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def createUser(self, user: User):
        try:
            query = "INSERT INTO User (userId, username, password, role) VALUES (%s, %s, %s, %s)"
            values = (user.userId, user.username, user.password, user.role)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("User created successfully.")
        except mysql.connector.Error as e:
            print("Error creating user:", e)

    def createProduct(self, product: Product):
        try:
            query = "INSERT INTO Product (productId, productName, description, price, quantityInStock, type) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (
                product.productId, product.productName, product.description, product.price, product.quantityInStock,
                product.type)

            self.cursor.execute(query, values)
            self.conn.commit()

            print("Product created successfully.")
        except mysql.connector.Error as e:
            print(f"Error creating product: {e}")
            self.conn.rollback()

    def createOrder(self, user: User, products: list):
        try:
            # Start a transaction
            self.conn.start_transaction()

            # Check if the user exists
            self.cursor.execute("SELECT * FROM User WHERE userId = %s", (user.userId,))
            user_exists = self.cursor.fetchone()

            if not user_exists:
                # If user does not exist, create the user
                self.createUser(user)

            # Check if products exist and are in stock
            for product in products:
                self.cursor.execute("SELECT * FROM Product WHERE productId = %s", (product.productId,))
                product_data = self.cursor.fetchone()
                if not product_data:
                    print(f"Product with ID {product.productId} does not exist.")
                    continue
                if product_data[4] < 1:  # Index 4 corresponds to quantityInStock
                    print(f"Product '{product.productName}' is out of stock.")
                    continue

                # Reduce the quantity in stock for the product
                new_quantity = product_data[4] - 1
                self.cursor.execute("UPDATE Product SET quantityInStock = %s WHERE productId = %s",
                                    (new_quantity, product.productId))

                # Insert the order into the Order table
                self.cursor.execute("INSERT INTO `Order` (userId, productId) VALUES (%s, %s)",
                                    (user.userId, product.productId))

                print(f"Order created successfully for product '{product.productName}'")

            # Commit the transaction
            self.conn.commit()

        except mysql.connector.Error as e:
            # Rollback the transaction if there's an error
            self.conn.rollback()
            print(f"Error creating order: {e}")

    def cancelOrder(self, userId: int, orderId: int):
        try:
            # Start a transaction
            self.conn.start_transaction()

            # Check if the order exists
            self.cursor.execute("SELECT * FROM `Order` WHERE userId = %s AND orderId = %s", (userId, orderId))
            order_exists = self.cursor.fetchone()

            if not order_exists:
                print(f"Order with ID {orderId} for user ID {userId} does not exist.")
            else:
                # Remove the order
                self.cursor.execute("DELETE FROM `Order` WHERE userId = %s AND orderId = %s", (userId, orderId))
                print(f"Order with ID {orderId} for user ID {userId} canceled successfully.")

            # Commit the transaction
            self.conn.commit()

        except mysql.connector.Error as e:
            # Rollback the transaction if there's an error
            self.conn.rollback()
            print(f"Error canceling order: {e}")

    def getAllProducts(self):
        try:
            # Retrieve all products from the Product table
            self.cursor.execute("SELECT * FROM Product")
            products = self.cursor.fetchall()
            return products

        except mysql.connector.Error as e:
            print(f"Error retrieving products: {e}")
            return []

    def getOrderByUser(self, user: User):
        try:
            # Execute SQL query to retrieve orders by user
            self.cursor.execute("SELECT * FROM `Order` WHERE userId = %s", (user.userId,))
            user_orders = self.cursor.fetchall()
            return user_orders

        except mysql.connector.Error as e:
            print(f"Error retrieving orders for user {user.username}: {e}")
            return []

    def close_connection(self):
        # Check if connection and cursor are available before closing
        if hasattr(self, 'cursor') and self.cursor is not None:
            self.cursor.close()
        if hasattr(self, 'conn') and self.conn.is_connected():
            self.conn.close()
            print('MySQL connection closed')

    def __del__(self):
        self.close_connection()

