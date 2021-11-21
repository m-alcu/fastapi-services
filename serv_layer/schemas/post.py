from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PostSchema(BaseModel):
    title: str = Field(..., title= "this is the post title", max_length=100)
    body: str = Field(..., title= "this is the post body", max_length=2000)
    is_published: bool = Field(..., title= "indicator is true for published posts")

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

