from sqlmodel import Session
from src.database.models import Kind, KindRead


def kind_by_id(kind_id: int, session: Session) -> KindRead:
    return session.get(Kind, kind_id)