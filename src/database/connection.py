from typing import Iterator
from sqlmodel import SQLModel, Session, create_engine

from src.config import config


connect_args = {"check_same_thread": False}
engine = create_engine(config.DB, echo=True, connect_args=connect_args)


def create_db_and_tables() -> None:  # pragma: no cover
    SQLModel.metadata.create_all(engine)


def get_session() -> Iterator[Session]:  # pragma: no cover
    with Session(engine) as session:
        yield session
