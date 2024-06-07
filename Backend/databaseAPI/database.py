from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pydantic import BaseModel
import random
from bson import ObjectId

# MongoDB connection
client = MongoClient("mongodb+srv://keithkishon2004:123@cluster0.vkyv4jx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.storygen_db

# Collections for different themes
collections = {
    "superhero": db["superhero"],
    "adventure": db["adventure"],
    "sport": db["sport"],
    "fairytale": db["fairytale"]
}

# Structure of what is stored in MongoDB
class Storygen(BaseModel):
    audio_url: str
    description: str

# Schemas
def individual_serial(storygen) -> dict:
    return {
        "id": str(storygen["_id"]),
        "audio_url": storygen["audio_url"],
        "description": storygen["description"]
    }

# List of all the audio URLs in a specific theme collection
def list_serial(collection) -> list:
    return [individual_serial(storygen) for storygen in collection.find()]

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Story Generator API"}

@app.get("/{theme}")
async def get_audio_url_by_theme(theme: str):
    if theme not in collections:
        raise HTTPException(status_code=404, detail="Theme not found")
    collection = collections[theme]
    urls = list_serial(collection)
    if not urls:
        raise HTTPException(status_code=404, detail="No audio URLs found for this theme")
    selected_audio = random.choice(urls)
    return {"audio_url": selected_audio['audio_url'], "description": selected_audio['description']}

@app.post("/{theme}")
async def post_storygen(theme: str, storygen: Storygen):
    if theme not in collections:
        raise HTTPException(status_code=404, detail="Theme not found")
    collection = collections[theme]
    collection.insert_one(dict(storygen))
    return {"message": "Audio URL added successfully"}

@app.put("/{theme}/{storygen_id}")
async def update_storygen(theme: str, storygen_id: str, updated_storygen: Storygen):
    if theme not in collections:
        raise HTTPException(status_code=404, detail="Theme not found")
    collection = collections[theme]
    result = collection.update_one({"_id": ObjectId(storygen_id)}, {"$set": updated_storygen.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Storygen not found")
    return {"message": "Storygen updated successfully"}

@app.delete("/{theme}/{storygen_id}")
async def delete_storygen(theme: str, storygen_id: str):
    if theme not in collections:
        raise HTTPException(status_code=404, detail="Theme not found")
    collection = collections[theme]
    try:
        obj_id = ObjectId(storygen_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    result = collection.delete_one({"_id": obj_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Storygen not found")
    return {"message": "Storygen deleted successfully"}
