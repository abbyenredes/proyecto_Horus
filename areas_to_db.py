from create_grid import create_grid
from pymongo import MongoClient

client = MongoClient('mongodb+srv://admin:Password@cluster0.j9n8ymo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['madrid42']
coleccion = db['locations']
area_centers = create_grid()[2]

for area in area_centers:
    coleccion.insert_one({
        'area': {
            'latitude': area[0],
            'longitude': area[1],
        },
    })