class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def update_order_status(self, order_id, new_status):
        for order in self.orders:
            if order.order_id == order_id:
                order.status = new_status
                return
        raise ValueError("Order not found.")

    def cancel_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)
                return
        raise ValueError("Order not found.")

    def get_order_details(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return {
                    'order_id': order.order_id,
                    'customer_id': order.customer_id,
                    'order_date': order.order_date,
                    'total_amount': order.total_amount,
                    'status': order.status
                }
        raise ValueError("Order not found.")
