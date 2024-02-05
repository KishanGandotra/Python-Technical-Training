class Products:
    def __init__(self, product_id, product_name, description, price, quantity_in_stock=0):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price
        self.__quantity_in_stock = quantity_in_stock

    # Properties for product attributes
    @property
    def product_id(self):
        return self.__product_id

    @property
    def product_name(self):
        return self.__product_name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    # Setter methods with data validation
    @product_name.setter
    def product_name(self, new_product_name):
        if isinstance(new_product_name, str):
            self.__product_name = new_product_name
        else:
            raise ValueError("Product name must be a string.")

    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str):
            self.__description = new_description
        else:
            raise ValueError("Description must be a string.")

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, (int, float)) and new_price >= 0:
            self.__price = new_price
        else:
            raise ValueError("Price must be a non-negative number.")

    @quantity_in_stock.setter
    def quantity_in_stock(self, new_quantity_in_stock):
        if isinstance(new_quantity_in_stock, int) and new_quantity_in_stock >= 0:
            self.__quantity_in_stock = new_quantity_in_stock
        else:
            raise ValueError("Quantity in stock must be a non-negative integer.")
