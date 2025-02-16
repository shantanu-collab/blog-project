from pydantic import BaseModel
from datetime import date


class postContent(BaseModel):
    text: str
    date: date
    userName : str
    
