class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def update_customer_info(self, customer_id, new_info):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                # Example: Update email, phone, or address
                if 'email' in new_info:
                    customer.email = new_info['email']
                if 'phone' in new_info:
                    customer.phone = new_info['phone']
                if 'address' in new_info:
                    customer.address = new_info['address']
                return
        raise ValueError("Customer not found.")

    def calculate_total_orders(self, customer_id):
        total_orders = 0
        for order in orders:
            if order.customer_id == customer_id:
                total_orders += 1
        return total_orders

    def get_customer_details(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return {
                    'customer_id': customer.customer_id,
                    'first_name': customer.first_name,
                    'last_name': customer.last_name,
                    'email': customer.email,
                    'phone': customer.phone,
                    'address': customer.address
                }
        raise ValueError("Customer not found.")
