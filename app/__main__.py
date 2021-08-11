import uvicorn

from app.infrastructure.presentation.fastapi import endpoints
from app.infrastructure.presentation.fastapi.app import create_fastapi_app

if __name__ == '__main__':
    app = create_fastapi_app(routers=[endpoints.api_router])
    uvicorn.run(app)
