from app.application.uow import UnitOfWork


def get_user_by_id(user_id: str, uow: UnitOfWork):
    with uow:
        found_user = uow.repo.get(id=user_id)
        if not found_user:
            raise
        return found_user
