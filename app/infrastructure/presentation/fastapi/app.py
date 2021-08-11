from typing import List

from fastapi import FastAPI, APIRouter


def create_fastapi_app(routers: List[APIRouter]):
    app = FastAPI()
    for router in routers:
        app.include_router(router)
    return app
