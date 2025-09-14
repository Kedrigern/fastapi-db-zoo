from sqlmodel import Session, select
from src.database.models import Kind, KindWrite


def kind_all(session: Session) -> list[Kind]:
    return session.exec(select(Kind)).all()


def kind_by_id(kind_id: int, session: Session) -> Kind | None:
    return session.get(Kind, kind_id)


def kind_add(kind: Kind, session: Session) -> Kind:
    session.add(kind)
    session.commit()
    session.refresh(kind)
    return kind