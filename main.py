import asyncio
import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import config as config

from load_router import ROUTE_LIST


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for route in ROUTE_LIST:
    app.include_router(route['route'], tags=route['tags'], prefix=route['prefix'])

@app.get("/",tags = ["Welcome"])
async def welcome():
    return {"message":"Welcome to livesstream status event"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)