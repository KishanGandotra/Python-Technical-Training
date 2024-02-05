from EXCEPTIONS import InsufficientStockException

class InventoryManager:
    def __init__(self):
        self.inventory = {}




    def add_to_inventory(self, product_id, quantity):
        if product_id in self.inventory:
            self.inventory[product_id] += quantity
        else:
            self.inventory[product_id] = quantity

    def remove_from_inventory(self, product_id, quantity):
        if product_id in self.inventory:
            if self.inventory[product_id] >= quantity:
                self.inventory[product_id] -= quantity
            else:
                raise InsufficientStockException("Insufficient stock for product {}".format(product_id))
        else:
            raise ValueError("Product not found in inventory.")

    def update_stock_quantity(self, product_id, new_quantity):
        self.inventory[product_id] = new_quantity

    def is_product_available(self, product_id, quantity_to_check):
        if product_id in self.inventory:
            return self.inventory[product_id] >= quantity_to_check
        return False

    def get_inventory_value(self):
        total_value = 0
        for product_id, quantity in self.inventory.items():
            # Assuming each product has a price attribute
            total_value += quantity * products[product_id].price
        return total_value

    def list_low_stock_products(self, threshold):
        low_stock_products = []
        for product_id, quantity in self.inventory.items():
            if quantity < threshold:
                low_stock_products.append(product_id)
        return low_stock_products

    def list_out_of_stock_products(self):
        out_of_stock_products = []
        for product_id, quantity in self.inventory.items():
            if quantity == 0:
                out_of_stock_products.append(product_id)
        return out_of_stock_products

    def list_all_products(self):
        return self.inventory
