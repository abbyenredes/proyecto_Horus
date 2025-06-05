from pymongo import MongoClient
from datetime import datetime, timezone

uri = "mongodb+srv://admin:"
client = MongoClient(uri)
# Base de datos y colección
db = client["madrid42"]

users = db["users"]

customer_phone_number = "+34"

users.insert_one({"_id": customer_phone_number,
                  "location": {
                      'latitude': 40.4168,
                      'longitude': -3.7038,
                      'timestamp': datetime.now(timezone.utc)
                  }})
