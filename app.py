from flask import Flask, request, jsonify
from database import get_db_connection

app = Flask(__name__)

@app.route('/update_parking', methods=['POST'])
def update_parking():
    try:
        # Extract the JSON data sent from the Android app
        data = request.get_json()
        latitude = data['latitude']
        longitude = data['longitude']
        parking_available = data['parkingAvailable']

        # Get database connection
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO parking_locations (latitude, longitude, parking_available)
            VALUES (%s, %s, %s)
        ''', (latitude, longitude, parking_available))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Parking information updated successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
