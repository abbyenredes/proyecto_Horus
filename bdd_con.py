from pymongo import MongoClient, DESCENDING

# Conectar a MongoDB
uri = "mongodb+srv://admin:Password@cluster0.j9n8ymo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

# Seleccionar la base de datos y colección
db = client["madrid42"]
collection = db["users"]

for doc in collection.find().limit(5):
    print(doc)