from abc import ABC, abstractmethod

from app.adapters import repository


class UnitOfWork(ABC):
    repo = repository.Repository

    def __enter__(self) -> ...:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

    @abstractmethod
    def refresh(self, entity: ...):
        pass


class SqliteUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: ...):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.user_repo = repository.SqliteUserRepository(self.session)
        self.post_repo = repository.SqlitePostRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def refresh(self, entity):
        self.session.refresh(entity)
