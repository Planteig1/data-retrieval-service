# Data retrieval service
from flask import Flask, jsonify

import requests
import csv

#Allows the end-user to retrieve data 
app = Flask(__name__)

#Bookings dataset
@app.route('/dataset/bookings', methods=["GET"])
def get_bookings_dataset():
    
    data = requests.get("http://booking-service:5000/booking/data")

    if data.status_code == 400:
        return "Couldnt get the data", 400

    bookings_data = data.json()

    #Define columns
    headers = [
            "booking_id", "days_rented", "season", "price",
            "room_number", "guest_id", "number_of_guests",
            "start_date", "end_date"
        ]
    
    
    with open('/app/data/bookings.csv', 'w', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(bookings_data)

    return "File downloaded successfully :)", 200



# Guest dataset
@app.route('/dataset/guests', methods=["GET"])
def get_guests_dataset():
    
    data = requests.get("http://guests-service:5000/guests/data")

    if data.status_code == 400:
        return "Couldnt get the data", 400

    data_json = data.json()

    #Define columns
    headers = ["id", "first_name", "last_name", "country"]
    
    with open('/app/data/guests.csv', 'w', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data_json)

    return "File downloaded successfully :)", 200


#Bills dataset
@app.route('/dataset/bills', methods=["GET"])
def get_bills_dataset():
    
    data = requests.get("http://bills-service:5000/bills/data")

    if data.status_code == 400:
        return "Couldnt get the data", 400

    data_json = data.json()

    #Define columns
    headers = ["guest_id", "item", "price", "paid_status", "bill_id"]
    
    with open('/app/data/bills.csv', 'w', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data_json)

    return "File downloaded successfully :)", 200



#Room pricing dataset
@app.route('/dataset/room-pricing', methods=["GET"])
def get_room_pricing_dataset():
    
    data = requests.get("http://room-pricing-service:5000/room-pricing/data")

    if data.status_code == 400:
        return "Couldnt get the data", 400

    data_json = data.json()

    #Define columns
    headers = ["room_type", "season", "daily_price"]
    
    with open('/app/data/room-pricing.csv', 'w', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data_json)

    return "File downloaded successfully :)", 200

#Rooms dataset

@app.route('/dataset/rooms', methods=["GET"])
def get_rooms_dataset():
    
    data = requests.get("http://room-service:5000/rooms/data")

    if data.status_code == 400:
        return "Couldnt get the data", 400

    data_json = data.json()

    #Define columns
    headers = ["room_number", "room_type", "availability", "cleaned_status"]
    
    with open('/app/data/rooms.csv', 'w', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data_json)

    return "File downloaded successfully :)", 200


app.run(debug=True, host="0.0.0.0")