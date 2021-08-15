from app.infrastructure.dependencies.container import ApplicationBaseContainer, ApplicationConfig
import uvicorn

from app.infrastructure.presentation.fastapi import endpoints
from app.infrastructure.presentation.fastapi.app import create_fastapi_app
from app.domain.models import Base

if __name__ == '__main__':
    container = ApplicationBaseContainer()
    container.config.from_pydantic(ApplicationConfig())
    container.wire([endpoints])
    app = create_fastapi_app(routers=[endpoints.api_router])
    app.container = container

    @app.on_event("startup")
    async def startup_event():
        Base.metadata.create_all(container.engine())
    

    uvicorn.run(app)
