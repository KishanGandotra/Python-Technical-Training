class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_product_info(self, product_id, new_info):
        for product in self.products:
            if product.product_id == product_id:
                # Example: Update name, description, or price
                if 'name' in new_info:
                    product.name = new_info['name']
                if 'description' in new_info:
                    product.description = new_info['description']
                if 'price' in new_info:
                    product.price = new_info['price']
                return
        raise ValueError("Product not found.")

    def is_product_in_stock(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product.quantity > 0
        return False

    def get_product_details(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return {
                    'product_id': product.product_id,
                    'name': product.name,
                    'description': product.description,
                    'price': product.price,
                    'quantity': product.quantity
                }
        raise ValueError("Product not found.")
