import mysql.connector

class DBConnection:
    __connection = None

    @staticmethod
    def getConnection():
        if not DBConnection.__connection:
            # Read connection properties from a property file
            # Replace these with your actual connection details
            connection_properties = {
                'host': 'localhost',
                'user': 'root',
                'password': 'root',
                'database': 'cars'
            }
            DBConnection.__connection = mysql.connector.connect(**connection_properties)
        return DBConnection.__connection
