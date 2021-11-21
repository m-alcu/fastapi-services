from fastapi import APIRouter, Depends, HTTPException, Path
from schemas.post import PostSchema, PostDB
from typing import List
from services.post import Post as ServicePost
import json

router = APIRouter()

@router.get("/post", response_model=List[PostDB])
def get_all_post():
    db_posts = ServicePost.get_all()
    return json.loads(db_posts.text)

@router.post("/post", status_code=201)
def create_post(post: PostSchema):
    result = ServicePost.create(**post.dict())
    return json.loads(result.text)

@router.get("/post/{id}", response_model=PostDB)
def get_post(id: int = Path(..., gt=0),):
    post = ServicePost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return json.loads(post.text)

@router.put("/post/{id}", response_model=None)
def modify_post(payload: PostSchema, id: int = Path(..., gt=0),):
    post = ServicePost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    ServicePost.put(id, **payload.dict())
    
@router.delete("/post/{id}", response_model=None)
def delete_post(id: int = Path(..., gt=0)):
    post = ServicePost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    ServicePost.delete(id)