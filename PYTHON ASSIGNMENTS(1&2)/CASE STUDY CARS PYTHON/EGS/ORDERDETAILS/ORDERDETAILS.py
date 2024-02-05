class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity = quantity

    # Properties for order detail attributes
    @property
    def order_detail_id(self):
        return self.__order_detail_id

    @property
    def order(self):
        return self.__order

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    # Setter methods with data validation
    @quantity.setter
    def quantity(self, new_quantity):
        if isinstance(new_quantity, int) and new_quantity > 0:
            self.__quantity = new_quantity
        else:
            raise ValueError("Quantity must be a positive integer.")

    def calculate_subtotal(self):
        return self.__quantity * self.__product.price
