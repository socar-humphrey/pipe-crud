from app.infrastructure.presentation.fastapi.schema import (
    UserRegisterOutSchema,
    UserRegisterSchema,
)
from app.infrastructure.dependencies.container import ApplicationBaseContainer
from fastapi import APIRouter, Depends

from app.application.uow import UnitOfWork
from app.application.usecases import delete_user_by_user_id, get_user_by_id, sign_up
from dependency_injector.wiring import Provide, inject

api_router = APIRouter(prefix="/api/v1")


@api_router.get("/users/{user_id}")
@inject
def get_user(
    user_id: str, uow: UnitOfWork = Depends(Provide[ApplicationBaseContainer.uow])
):
    return get_user_by_id(user_id=user_id, uow=uow)


@api_router.post("/users", response_model=UserRegisterOutSchema)
@inject
def add_user(
    request: UserRegisterSchema,
    uow: UnitOfWork = Depends(Provide[ApplicationBaseContainer.uow]),
):
    res = sign_up(username=request.username, password=request.password, uow=uow)
    return res


@api_router.delete("/users/{user_id}")
@inject
def delete_user(
    user_id: str, uow: UnitOfWork = Depends(Provide[ApplicationBaseContainer.uow])
):
    delete_user_by_user_id(user_id=user_id, uow=uow)


@api_router.get("/posts/{post_id}")
def get_posts_by_id(post_id: str):
    pass


@api_router.post("/posts")
def create_post(post_id: str):
    pass


@api_router.get("/posts")
def get_posts_by_user_id(user_id: str):
    pass


@api_router.delete("/posts/{post_id}")
def delete_post(post_id: str):
    pass
