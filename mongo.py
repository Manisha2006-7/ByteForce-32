from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["invoices"]
collection = db["records"]

def save_to_mongo(data):
    collection.insert_one(data)
