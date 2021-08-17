import ulid
from app.domain.models import User
from app.application.uow import UnitOfWork
from fastapi import status


class UseCaseError(Exception):
    def __init__(
        self, message: str, code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    ) -> None:
        self.message = message
        self.code = code

    def __str__(self) -> str:
        return f"UseCaseError({self.code}): {self.message}"


def get_user_by_id(user_id: str, uow: UnitOfWork) -> User:
    with uow:
        found_user = uow.user_repo.get(id=user_id)
        if not found_user:
            raise UseCaseError(message="유저를 찾을 수 없습니다")
        return found_user


def delete_user_by_user_id(user_id: str, uow: UnitOfWork) -> None:
    with uow:
        found_user = uow.user_repo.get(id=user_id)
        if not found_user:
            raise UseCaseError(message="유저를 찾을 수 없습니다")
        uow.user_repo.delete(id=user_id)
        uow.commit()


def sign_up(username: str, password: str, uow: UnitOfWork) -> User:
    with uow:
        new_user = User(id=ulid.new().str, name=username, password=password)
        uow.user_repo.add(new_user)
        uow.commit()
        return new_user # FIXME(humphrey): detached instance
