from fastapi import FastAPI
from api.v1_00.api import api_router

app = FastAPI(title="Async FastAPI")

app.include_router(api_router, prefix="/api")
