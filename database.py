import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='mysql-7698aa2-ymreddy-7959.h.aivencloud.com',  # Replace with your DB host
            user='avnadmin',  # Replace with your DB username
            password='AVNS_ATKsEXAR4RM2Wn1CkYR',  # Replace with your DB password
            database='parking_db'  # Replace with your DB name
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None
