class InvalidDataException(Exception):
    pass

class InsufficientStockException(Exception):
    pass

class IncompleteOrderException(Exception):
    pass

class PaymentFailedException(Exception):
    pass

class FileIOException(Exception):
    pass

class DatabaseAccessException(Exception):
    pass

class ConcurrencyException(Exception):
    pass

class AuthenticationException(Exception):
    pass

class AuthorizationException(Exception):
    pass

class Order:
    def __init__(self, order_id, quantity):
        self.order_id = order_id
        self.quantity = quantity

class Inventory:
    def __init__(self, available_stock):
        self.available_stock = available_stock

    def process_order(self, order):
        if order.quantity > self.available_stock:
            raise InsufficientStockException("Insufficient stock to fulfill the order.")

class OrderProcessor:
    def __init__(self, inventory):
        self.inventory = inventory

    def process_order(self, order):
        try:
            self.inventory.process_order(order)
            print("Order processed successfully.")
        except InsufficientStockException as e:
            print(f"Error processing order: {e}")

if __name__ == "__main__":
    inventory = Inventory(10)
    order = Order(1, 15)  # Attempting to order more than available stock

    order_processor = OrderProcessor(inventory)
    order_processor.process_order(order)
