from pydantic import BaseModel

class Storygen(BaseModel):
    audio_url: str 
    description: str
    
            