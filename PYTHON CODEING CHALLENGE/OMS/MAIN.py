from ORDER_PROCESSOR import OrderProcessor
from ORDER_MANAGEMENT_REPOSITORY import OrderManagementRepository
from USER import User
from PRODUCT import Product

class OrderManagement:
    def __init__(self):
        self.order_processor = OrderProcessor()
        self.order_management_repository = OrderManagementRepository()

    def main(self):
        print("Welcome to the Order Management System")

        while True:
            print("\nMenu:")
            print("1. Create User")
            print("2. Create Product")
            print("3. Cancel Order")
            print("4. Get All Products")
            print("5. Get Order by User")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.createUser()
            elif choice == "2":
                self.createProduct()
            elif choice == "3":
                self.cancelOrder()
            elif choice == "4":
                self.getAllProducts()
            elif choice == "5":
                self.getOrderbyUser()
            elif choice == "6":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def createUser(self):
        userId = int(input("Enter user ID: "))
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (Admin/User): ")

        user = User(userId, username, password, role)
        self.order_management_repository.createUser(user)

        print("User created successfully.")

    def createProduct(self):
        productId = int(input("Enter product ID: "))
        productName = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        quantityInStock = int(input("Enter quantity in stock: "))
        type = input("Enter product type (Electronics/Clothing): ")

        product = Product(productId, productName, description, price, quantityInStock, type)
        self.order_management_repository.createProduct(product)

        print("Product created successfully.")

    def cancelOrder(self):
        userId = int(input("Enter user ID: "))
        orderId = int(input("Enter order ID: "))

        self.order_management_repository.cancelOrder(userId, orderId)
        print("Order canceled successfully.")

    def getAllProducts(self):
        products = self.order_management_repository.getAllProducts()
        for product in products:
            print(product)

    def getOrderbyUser(self):
        userId = int(input("Enter user ID: "))
        user = User(userId, '', '', '')  # Create a dummy User object with the userId
        orders = self.order_management_repository.getOrderByUser(user)
        for order in orders:
            print(order)
if __name__ == "__main__":
    order_management = OrderManagement()
    order_management.main()
