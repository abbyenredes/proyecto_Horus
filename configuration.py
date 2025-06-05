from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Configuración de conexión a MongoDB
uri = "mongodb+srv://admin:"
client = MongoClient(uri)
# Base de datos y colección
db = client["madrid42"]  # replace with your DB name
areas_collection = db["areas"]
