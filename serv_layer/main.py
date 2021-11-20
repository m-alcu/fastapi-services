import uvicorn
from models import Post as ModelPost
from schema import PostSchema, PostDB
from app import app
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Path


@app.get("/post/", response_model=List[PostDB])
async def get_all_post():
    db_posts = await ModelPost.get_all()
    return list(map(lambda db_post: PostDB(**db_post), db_posts))

@app.post("/post/")
async def create_post(post: PostSchema):
    post_id = await ModelPost.create(**post.dict())
    return {"user_id": post_id}


@app.get("/post/{id}", response_model=PostDB)
async def get_post(id: int):
    post = await ModelPost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return PostDB(**post).dict()

@app.put("/post/{id}/", response_model=None)
async def modify_post(payload: PostSchema, id: int = Path(..., gt=0),):
    post = await ModelPost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await ModelPost.put(id, **payload.dict())
    
@app.delete("/post/{id}/", response_model=None)
async def delete_post(id: int = Path(..., gt=0)):
    post = await ModelPost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await ModelPost.delete(id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
