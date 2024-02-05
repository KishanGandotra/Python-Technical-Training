class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock
        self.__last_stock_update = last_stock_update

    # Properties for inventory attributes
    @property
    def inventory_id(self):
        return self.__inventory_id

    @property
    def product(self):
        return self.__product

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    @property
    def last_stock_update(self):
        return self.__last_stock_update

    # Setter methods with data validation
    @quantity_in_stock.setter
    def quantity_in_stock(self, new_quantity_in_stock):
        if isinstance(new_quantity_in_stock, int) and new_quantity_in_stock >= 0:
            self.__quantity_in_stock = new_quantity_in_stock
        else:
            raise ValueError("Quantity in stock must be a non-negative integer.")

    @last_stock_update.setter
    def last_stock_update(self, new_last_stock_update):
        self.__last_stock_update = new_last_stock_update
