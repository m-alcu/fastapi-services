from fastapi import APIRouter, Depends, HTTPException, Path
from schemas.post import PostSchema, PostDB
from typing import List
from services.post import Post as ServicePost

router = APIRouter()

@router.get("/post", response_model=List[PostDB])
async def get_all_post():
    db_posts = await ServicePost.get_all()
    return list(map(lambda db_post: PostDB(**db_post), db_posts))

@router.post("/post", status_code=201)
async def create_post(post: PostSchema):
    post_id = await ServicePost.create(**post.dict())
    return {"id": post_id}


@router.get("/post/{id}", response_model=PostDB)
async def get_post(id: int = Path(..., gt=0),):
    post = await ServicePost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return PostDB(**post).dict()

@router.put("/post/{id}", response_model=None)
async def modify_post(payload: PostSchema, id: int = Path(..., gt=0),):
    post = await ServicePost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await ServicePost.put(id, **payload.dict())
    
@router.delete("/post/{id}", response_model=None)
async def delete_post(id: int = Path(..., gt=0)):
    post = await ServicePost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await ServicePost.delete(id)