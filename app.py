from flask import Flask, request, jsonify
from database import save_parking_data

app = Flask(__name__)

@app.route('/save_parking', methods=['POST'])
def save_parking():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    has_parking = data.get('has_parking')

    if save_parking_data(latitude, longitude, has_parking):
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "failure"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
