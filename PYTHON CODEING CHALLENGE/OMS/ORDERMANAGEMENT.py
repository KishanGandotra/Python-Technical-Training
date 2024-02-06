from ORDER_PROCESSOR import OrderProcessor
from USER import User
from PRODUCT import Product

class OrderManagement:
    @staticmethod
    def main():
        order_processor = OrderProcessor()

        while True:
            print("\n===== Order Management System =====")
            print("1. Create User")
            print("2. Create Product")
            print("3. Create Order")
            print("4. Cancel Order")
            print("5. Get All Products")
            print("6. Get Orders by User")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                userId = int(input("Enter user ID: "))
                username = input("Enter username: ")
                password = input("Enter password: ")
                role = input("Enter role (Admin/User): ")

                user = User(userId, username, password, role)
                order_processor.createUser(user)

            elif choice == '2':
                productId = int(input("Enter product ID: "))
                productName = input("Enter product name: ")
                description = input("Enter product description: ")
                price = float(input("Enter product price: "))
                quantityInStock = int(input("Enter quantity in stock: "))
                type = input("Enter product type (Electronics/Clothing): ")

                product = Product(productId, productName, description, price, quantityInStock, type)
                order_processor.createProduct(product)  # Ensure product argument is passed here

            elif choice == '3':
                userId = int(input("Enter user ID: "))
                # Fetch products from the database or create a list of products manually
                products = []  # Add products to this list
                order_processor.createOrder(User(userId, "", "", ""), products)

            elif choice == '4':
                userId = int(input("Enter user ID: "))
                orderId = int(input("Enter order ID: "))
                order_processor.cancelOrder(userId, orderId)

            elif choice == '5':
                order_processor.getAllProducts()

            elif choice == '6':
                userId = int(input("Enter user ID: "))
                order_processor.getOrderByUser(User(userId, "", "", ""))

            elif choice == '7':
                print("Exiting the Order Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    OrderManagement.main()
