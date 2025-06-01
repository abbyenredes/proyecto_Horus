from opengateway_sandbox_sdk import ClientCredentials, DeviceLocation
from pymongo import MongoClient
import time

credentials = ClientCredentials(
    client_id = '0f57c7b9-9d68-497d-95ea-5ed4e589484c',
    client_secret = '5f7e0446-5c2b-4307-b1ad-b26f833009be'
)

customer_phone_number = "+34646609563"

devicelocation_client = DeviceLocation(credentials=credentials, phone_number=customer_phone_number)

# result = devicelocation_client.verify(40, -3, 4, customer_phone_number)  # as set in the authorization step
#
# print(f"Is the device in location? {result}")

for i in range(1):
    result = devicelocation_client.verify(40.5150, -3.6340, 3, customer_phone_number)
    if result:
        print("OK")
    else:
        print(f"Not OK {i}")
    # time.sleep(1)

# for i in range(2, 20):
#     result = devicelocation_client.verify(40.5150, -3.6340, i, customer_phone_number)
#     print(result)
#     if result:
#         print(f"Detected at {result} km")
# uri = "mongodb+srv://admin:Password@cluster0.j9n8ymo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#
# client = MongoClient(uri)
# db = client["madrid42"]
