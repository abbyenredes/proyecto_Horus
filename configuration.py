from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Configuración de conexión a MongoDB
uri = "mongodb+srv://admin:Password@cluster0.j9n8ymo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
# Base de datos y colección
db = client["madrid42"]  # replace with your DB name
areas_collection = db["areas"]