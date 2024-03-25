from re import A
from bson import ObjectId
from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pydantic import BaseModel


# Linking to MongoDB Atlas
client = MongoClient(
    "mongodb+srv://keithkishon2004:123@cluster0.vkyv4jx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
db = client.storygen_db
collection_name = db["storygen_collection"]


# Structure of the whatever is stored in MongoDB
class Storygen(BaseModel):
    audio_url: str
    description: str
    # name: str
    # description: str
    # complete: bool


# Schemas
def individual_serial(storygen) -> dict:
    return {
        "id": str(storygen["_id"]),
        "audio_url": storygen["audio_url"],
        "description": storygen["description"],
        # "id": str(storygen["_id"]),
        # "name": storygen["name"],
        # "description": storygen["description"],
        # "complete": storygen["complete"],
    }


# def list_serial(storygens) -> list:
#     return [individual_serial(storygen) for storygen in storygens]


def list_serial() -> list:
    return [individual_serial(storygen) for storygen in collection_name.find()]


app = FastAPI()
# router = APIRouter()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def audio_URLs():
    urls = list_serial()
    return {"message": urls}


@app.post("/")
async def post_storygen(storygen: Storygen):
    collection_name.insert_one(dict(storygen))


@app.put("/{storygen_id}")
async def update_storygen(storygen_id: str, updated_storygen: Storygen):
    result = collection_name.update_one({"_id": ObjectId(storygen_id)}, {"$set": updated_storygen.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Storygen not found")
    return {"message": "Storygen updated successfully"}




@app.delete("/{storygen_id}")
async def delete_storygen(storygen_id: str):
    try:
        obj_id = ObjectId(storygen_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid ObjectId")

    result = collection_name.delete_one({"_id": obj_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Storygen not found")
    return {"message": "Storygen deleted successfully"}