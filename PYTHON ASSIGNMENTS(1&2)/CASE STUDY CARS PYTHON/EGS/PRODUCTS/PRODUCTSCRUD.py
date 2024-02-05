class ProductsCRUD:
    def __init__(self, connector):
        self.connector = connector

    def create_product(self, product_data):
        query = "INSERT INTO products (product_name, description, price) VALUES (%s, %s, %s)"
        data = (product_data['product_name'], product_data['description'], product_data['price'])

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Product created successfully")
        except mysql.connector.Error as e:
            print(f"Error creating product: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def read_product(self, product_id):
        query = "SELECT * FROM products WHERE product_id = %s"
        data = (product_id,)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor(dictionary=True)
            cursor.execute(query, data)
            product = cursor.fetchone()
            if product:
                print("Product details:")
                print(product)
            else:
                print("Product not found")
        except mysql.connector.Error as e:
            print(f"Error reading product: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def update_product(self, product_id, new_product_data):
        query = "UPDATE products SET product_name = %s, description = %s, price = %s WHERE product_id = %s"
        data = (new_product_data['product_name'], new_product_data['description'], new_product_data['price'], product_id)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Product updated successfully")
        except mysql.connector.Error as e:
            print(f"Error updating product: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE product_id = %s"
        data = (product_id,)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Product deleted successfully")
        except mysql.connector.Error as e:
            print(f"Error deleting product: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()
