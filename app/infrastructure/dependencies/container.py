from app.application.uow import SqliteUnitOfWork
import sqlalchemy

from enum import Enum
from dependency_injector import providers
from pydantic import BaseSettings, Field
from dependency_injector.containers import DeclarativeContainer


class ApplicationEnvironment(str, Enum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


class DatabaseConfig(BaseSettings):
    uri: str = Field(default="sqlite:///./pipe.db", env="db_uri")



class ApplicationConfig(BaseSettings):
    db = DatabaseConfig()
    env: ApplicationEnvironment = Field(
        env="app_env", default=ApplicationEnvironment.DEV
    )


class ApplicationBaseContainer(DeclarativeContainer):
    config = providers.Configuration()
    engine = providers.Singleton(sqlalchemy.create_engine, config.db.uri, echo=True)
    session = providers.Singleton(
        sqlalchemy.orm.sessionmaker, autocommit=False, autoflush=False, bind=engine
    )
    session_factory = providers.Singleton(sqlalchemy.orm.scoped_session, session)
    uow = providers.Factory(SqliteUnitOfWork, session_factory=session_factory)
