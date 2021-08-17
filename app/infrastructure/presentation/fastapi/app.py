from starlette.responses import JSONResponse
from app.application.usecases import UseCaseError
from typing import List

from fastapi import FastAPI, APIRouter, Request, Response


def create_fastapi_app(routers: List[APIRouter]):
    app = FastAPI()
    for router in routers:
        app.include_router(router)

    @app.exception_handler(UseCaseError)
    async def handle_usecase_error(request: Request, exc: UseCaseError) -> Response:
        return JSONResponse(
            status_code=exc.code, content={"message": exc.message, "code": exc.code}
        )

    return app
