from typing import Iterator
from sqlmodel import SQLModel, Session, create_engine


connect_args = {"check_same_thread": False}
engine = create_engine("sqlite:///test.db", echo=True, connect_args=connect_args)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session