# db_util.py
import mysql.connector

class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="oms"
            )
            return conn
        except mysql.connector.Error as e:
            print("Error connecting to MySQL", e)
            return None
