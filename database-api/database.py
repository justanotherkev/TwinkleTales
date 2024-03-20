from re import A
from fastapi import FastAPI, APIRouter
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


def list_serial(storygens) -> list:
    return [individual_serial(storygen) for storygen in storygens]


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
async def story_gen():
    storygen = list_serial(collection_name.find())
    return {"message": storygen}


# @app.get("/start")
# async def story_gen():
#     storygen = list_serial(collection_name.find())
#     return {"message": storygen}


@app.post("/")
async def post_storygen(storygen: Storygen):
    collection_name.insert_one(dict(storygen))