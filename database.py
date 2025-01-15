import mysql.connector

def save_parking_data(latitude, longitude, has_parking):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='your-database-host',
            user='your-database-user',
            password='your-database-password',
            database='your-database-name'
        )

        cursor = connection.cursor()

        # SQL query to insert parking data
        query = "INSERT INTO parking_locations (latitude, longitude, has_parking) VALUES (%s, %s, %s)"
        cursor.execute(query, (latitude, longitude, has_parking))

        # Commit the transaction
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
