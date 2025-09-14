from sqlmodel import Session, select
from src.database.models import Kind, KindRead


def kind_all(session: Session) -> list[KindRead]:
    return session.exec(select(Kind)).all()


def kind_by_id(kind_id: int, session: Session) -> KindRead | None:
    return session.get(Kind, kind_id)
