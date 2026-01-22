# backend/api/app.py
from fastapi import FastAPI
from api.routes import ping, index, search

def create_app() -> FastAPI:
    app = FastAPI(title="Vector Image Finder")

    app.include_router(ping.router)
    app.include_router(index.router)
    app.include_router(search.router)

    return app
