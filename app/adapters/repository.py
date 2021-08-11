from abc import ABC, abstractmethod


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
        pass

    def add(self, entity: ...) -> ...:
        pass
