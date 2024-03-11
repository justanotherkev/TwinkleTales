from fastapi import APIRouter, FastAPI, HTTPException
from models.storygen import Storygen
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS settings at the FastAPI application level
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update this with your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

router = APIRouter()

# GET Request Method
@router.get("/")
async def story_gen():
    storygen = list_serial(collection_name.find())
    return storygen
    

# POST Request Method
@router.post("/")
async def post_storygen(storygen: Storygen):
    collection_name.insert_one(dict(storygen))

