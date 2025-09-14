from typing import Iterator
from datetime import datetime
from sqlmodel import SQLModel, Session, create_engine

from src.config import config
from src.database.models import Kind, Pet

connect_args = {"check_same_thread": False}
engine = create_engine(config.DB, echo=True, connect_args=connect_args)


def create_db_and_tables() -> None:  # pragma: no cover
    SQLModel.metadata.create_all(engine)
    if config.demo:
        with Session(engine) as session:
            fill_demo_data(session)


def get_session() -> Iterator[Session]:  # pragma: no cover
    with Session(engine) as session:
        yield session


def fill_demo_data(session: Session):  # pragma: no cover
    """
    Fill database with demo data
    """
    franchie = Kind(name="French Bulldog")
    session.add(franchie)
    boxer = Kind(name="Boxer")
    session.add(boxer)
    session.add(Kind(name="Persian cat"))
    session.commit()
    session.refresh(franchie)
    session.refresh(boxer)
    session.add(
        Pet(name="Arya", born=datetime.fromisoformat("2023-06-15"), kind_id=franchie.id)
    )
    session.add(
        Pet(name="Bruno", born=datetime.fromisoformat("2024-01-01"), kind_id=boxer.id)
    )
    session.commit()