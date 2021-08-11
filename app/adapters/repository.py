from abc import ABC, abstractmethod

from app.domain.models import User, Post


class Repository(ABC):
    @abstractmethod
    def get(self, id: str) -> ...:
        ...

    @abstractmethod
    def add(self, entity: ...) -> ...:
        ...


class SqliteRepository(Repository):

    def __init__(self, session: ...) -> None:
        self.session = session

    def get(self, id: str) -> ...:
        return self._get(id=id)

    def add(self, entity: ...) -> ...:
        return self._add(entity=entity)

    @abstractmethod
    def _get(self, id: str):
        pass

    @abstractmethod
    def _add(self, entity: ...) -> ...:
        pass


class SqliteUserRepository(SqliteRepository):
    def _get(self, id: str) -> User:
        return self.session.query(User).filter_by(id=id)

    def _add(self, entity: User) -> User:
        self.session.add(entity=entity)
        self.session.refresh(entity)
        self.session.commit()
        return entity


class SqlitePostRepository(SqliteRepository):
    def _get(self, id: str) -> Post:
        return self.session.query(Post).filter_by(id=id)

    def _add(self, entity: Post) -> Post:
        self.session.add(entity=entity)
        self.session.refresh(entity)
        self.session.commit()
        return entity
