from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostSchema(BaseModel):
    title: str
    body: str 
    is_published: bool

    class Config:
        orm_mode = True

class PostDB(BaseModel):
    id: int
    title: str
    body: str 
    is_published: bool
    created: Optional[datetime]
    modified: Optional[datetime]

    class Config:
        orm_mode = True

