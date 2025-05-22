import asyncio
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.endpoints.user import user_router
from api.endpoints.consultas import consulta_router
from fastapi.middleware.cors import CORSMiddleware


routes = [
    user_router,
    consulta_router
    ]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "¡Hola, FastAPI está funcionando!"}


for route in routes:
    app.include_router(route)
