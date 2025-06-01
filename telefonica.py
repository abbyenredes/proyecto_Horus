from opengateway_sandbox_sdk import ClientCredentials, DeviceLocation
# from configuration import db
from pymongo import MongoClient
from datetime import datetime, timezone

uri = "mongodb+srv://admin:Password@cluster0.j9n8ymo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["madrid42"]

credentials = ClientCredentials(
    client_id = '0f57c7b9-9d68-497d-95ea-5ed4e589484c',
    client_secret = '5f7e0446-5c2b-4307-b1ad-b26f833009be'
)

customer_phone_number = "+34646609563"

devicelocation_client = DeviceLocation(credentials=credentials, phone_number=customer_phone_number)

def update_user():
    locations = db["locations"]
    areas = locations.find({},{'_id': 0,'area': 1})
    for area in areas:
        lat = area['area']['latitude']
        lon = area['area']['longitude']
        result = devicelocation_client.verify(lat, lon, 3, customer_phone_number)
        if result:
            db['user'].update_one({'_id': customer_phone_number}, {'$push':
                                                                       {'location':
                                                                            {'latitude': lat,
                                                                             'longitude': lon,
                                                                             'timestamp': datetime.now(timezone.utc)}}})


update_user()