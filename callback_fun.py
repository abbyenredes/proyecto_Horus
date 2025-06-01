""" TODO: function to handle the callback from the orus API; gather the data and save it to the database
"""

from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
import httpx

app= FastAPI()

# --- MongoDB connection ---

MONGO_URI= "mongodb+srv://admin:Password@cluster0.j9n8ymo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client= MongoClient(MONGO_URI)
db= client["madrid42"]
users_collection= db["users"]

