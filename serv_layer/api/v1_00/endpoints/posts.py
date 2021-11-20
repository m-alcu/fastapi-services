from fastapi import APIRouter, Depends, HTTPException, Path
from schema import PostSchema, PostDB
from typing import List
from models.posts import Post as ModelPost

router = APIRouter()

@router.get("/post/", response_model=List[PostDB])
async def get_all_post():
    db_posts = await ModelPost.get_all()
    return list(map(lambda db_post: PostDB(**db_post), db_posts))

@router.post("/post/")
async def create_post(post: PostSchema):
    post_id = await ModelPost.create(**post.dict())
    return {"user_id": post_id}


@router.get("/post/{id}", response_model=PostDB)
async def get_post(id: int):
    post = await ModelPost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return PostDB(**post).dict()

@router.put("/post/{id}/", response_model=None)
async def modify_post(payload: PostSchema, id: int = Path(..., gt=0),):
    post = await ModelPost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await ModelPost.put(id, **payload.dict())
    
@router.delete("/post/{id}/", response_model=None)
async def delete_post(id: int = Path(..., gt=0)):
    post = await ModelPost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await ModelPost.delete(id)