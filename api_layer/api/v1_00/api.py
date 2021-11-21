from fastapi import APIRouter
from api.v1_00.endpoints import posts

api_router = APIRouter()
api_router.include_router(posts.router, tags=["post"])
