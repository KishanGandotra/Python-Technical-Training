from ORDER_MANAGEMENT_REPOSITORY import IOrderManagementRepository
from USER import User
from PRODUCT import Product
import DB_UTIL

class OrderProcessor(IOrderManagementRepository):
    def createOrder(self, user: User, products: list):
        conn = DB_UTIL.DBUtil.getDBConn()
        cursor = conn.cursor()

        try:
            # Check if the user already exists in the database
            cursor.execute("SELECT * FROM users WHERE userId = %s", (user.getUserId(),))
            existing_user = cursor.fetchone()

            if existing_user is None:
                # If user does not exist, create the user
                cursor.execute("INSERT INTO users (userId, username, password, role) VALUES (%s, %s, %s, %s)",
                               (user.getUserId(), user.getUsername(), user.getPassword(), user.getRole()))
                conn.commit()

            # Create order
            # Assume orders are stored in a table called 'orders' with orderId, userId, productId, quantity, etc.
            # The implementation depends on your database schema and design.
            # Insert orders into the orders table

            print("Order created successfully.")

        except Exception as e:
            conn.rollback()
            print("Error creating order:", e)

        finally:
            cursor.close()
            conn.close()

    def cancelOrder(self, userId: int, orderId: int):
        conn = DB_UTIL.DBUtil.getDBConn()
        cursor = conn.cursor()

        try:
            # Check if the order exists
            cursor.execute("SELECT * FROM orders WHERE userId = %s AND orderId = %s", (userId, orderId))
            existing_order = cursor.fetchone()

            if existing_order is None:
                print("Order not found.")
                return

            # Cancel the order
            # Delete the order from the orders table
            cursor.execute("DELETE FROM orders WHERE userId = %s AND orderId = %s", (userId, orderId))
            conn.commit()

            print("Order cancelled successfully.")

        except Exception as e:
            conn.rollback()
            print("Error cancelling order:", e)

        finally:
            cursor.close()
            conn.close()

    def createProduct(self, user: User, product: Product):
        conn = DB_UTIL.DBUtil.getDBConn()
        cursor = conn.cursor()

        try:
            # Check if the user is an admin
            if user.getRole() != "Admin":
                print("Only admins can create products.")
                return

            # Create product
            # Insert the product into the products table
            cursor.execute("INSERT INTO products (productId, productName, description, price, quantityInStock, type) "
                           "VALUES (%s, %s, %s, %s, %s, %s)",
                           (product.getProductId(), product.getProductName(), product.getDescription(),
                            product.getPrice(), product.getQuantityInStock(), product.getType()))
            conn.commit()

            print("Product created successfully.")

        except Exception as e:
            conn.rollback()
            print("Error creating product:", e)

        finally:
            cursor.close()
            conn.close()

    def createUser(self, user: User):
        conn = DB_UTIL.DBUtil.getDBConn()
        cursor = conn.cursor()

        try:
            # Create user
            cursor.execute("INSERT INTO users (userId, username, password, role) VALUES (%s, %s, %s, %s)",
                           (user.getUserId(), user.getUsername(), user.getPassword(), user.getRole()))
            conn.commit()

            print("User created successfully.")

        except Exception as e:
            conn.rollback()
            print("Error creating user:", e)

        finally:
            cursor.close()
            conn.close()

    def getAllProducts(self):
        conn = DB_UTIL.DBUtil.getDBConn()
        cursor = conn.cursor()

        try:
            # Retrieve all products from the products table
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

            for product in products:
                print(product)  # Print or process the product data as required

        except Exception as e:
            print("Error retrieving products:", e)

        finally:
            cursor.close()
            conn.close()

    def getOrderByUser(self, user: User):
        conn = DB_UTIL.DBUtil.getDBConn()
        cursor = conn.cursor()

        try:
            # Retrieve orders by user from the orders table
            cursor.execute("SELECT * FROM orders WHERE userId = %s", (user.getUserId(),))
            orders = cursor.fetchall()

            for order in orders:
                print(order)  # Print or process the order data as required

        except Exception as e:
            print("Error retrieving orders:", e)

        finally:
            cursor.close()
            conn.close()
