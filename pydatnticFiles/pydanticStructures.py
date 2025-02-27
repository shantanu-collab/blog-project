from pydantic import BaseModel
from datetime import date
from typing import Optional


class postContent(BaseModel):
    userName: str
    loginTime: Optional[str] = None
    logoutTime : Optional[str] = None
    
