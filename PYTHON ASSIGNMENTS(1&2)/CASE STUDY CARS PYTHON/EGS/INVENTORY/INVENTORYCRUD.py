class InventoryCRUD:
    def __init__(self, connector):
        self.connector = connector

    def create_inventory_item(self, inventory_data):
        query = "INSERT INTO inventory (product_id, quantity_in_stock, last_stock_update) VALUES (%s, %s, %s)"
        data = (inventory_data['product_id'], inventory_data['quantity_in_stock'], inventory_data['last_stock_update'])

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Inventory item created successfully")
        except mysql.connector.Error as e:
            print(f"Error creating inventory item: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def read_inventory_item(self, inventory_id):
        query = "SELECT * FROM inventory WHERE inventory_id = %s"
        data = (inventory_id,)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor(dictionary=True)
            cursor.execute(query, data)
            inventory_item = cursor.fetchone()
            if inventory_item:
                print("Inventory item details:")
                print(inventory_item)
            else:
                print("Inventory item not found")
        except mysql.connector.Error as e:
            print(f"Error reading inventory item: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def update_inventory_item(self, inventory_id, new_inventory_data):
        query = "UPDATE inventory SET product_id = %s, quantity_in_stock = %s, last_stock_update = %s WHERE inventory_id = %s"
        data = (new_inventory_data['product_id'], new_inventory_data['quantity_in_stock'], new_inventory_data['last_stock_update'], inventory_id)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Inventory item updated successfully")
        except mysql.connector.Error as e:
            print(f"Error updating inventory item: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()

    def delete_inventory_item(self, inventory_id):
        query = "DELETE FROM inventory WHERE inventory_id = %s"
        data = (inventory_id,)

        try:
            self.connector.connect()
            cursor = self.connector.connection.cursor()
            cursor.execute(query, data)
            self.connector.connection.commit()
            print("Inventory item deleted successfully")
        except mysql.connector.Error as e:
            print(f"Error deleting inventory item: {e}")
        finally:
            if self.connector.connection:
                cursor.close()
                self.connector.disconnect()
