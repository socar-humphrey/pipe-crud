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


class SqliteUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: ...):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.repo = repository.SqliteRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
