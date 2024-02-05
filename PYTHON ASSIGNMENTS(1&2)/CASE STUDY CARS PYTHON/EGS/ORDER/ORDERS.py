class Orders:
    def __init__(self, order_id, customer, order_date, total_amount, status="Pending"):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = order_date
        self.__total_amount = total_amount
        self.__status = status
        self.__order_details = []  # List to store order details

    # Properties for order attributes
    @property
    def order_id(self):
        return self.__order_id

    @property
    def customer(self):
        return self.__customer

    @property
    def order_date(self):
        return self.__order_date

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def status(self):
        return self.__status

    @property
    def order_details(self):
        return self.__order_details

    # Setter methods with data validation
    @status.setter
    def status(self, new_status):
        valid_statuses = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]
        if new_status in valid_statuses:
            self.__status = new_status
        else:
            raise ValueError("Invalid order status.")

    def add_order_detail(self, order_detail):
        self.__order_details.append(order_detail)

    def cancel_order(self):
        self.__status = "Cancelled"
