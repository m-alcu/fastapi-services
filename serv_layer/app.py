from db import db
from fastapi import FastAPI
from api.v1_00.api import api_router

app = FastAPI(title="Async FastAPI")

app.include_router(api_router, prefix="/api")

@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
