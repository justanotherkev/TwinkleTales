from pymongo import MongoClient

client = MongoClient("mongodb+srv://keithkishon2004:123@cluster0.vkyv4jx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.storygen_db

collection_name = db["storygen_collection"]
