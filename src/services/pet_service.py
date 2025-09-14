from sqlmodel import Session, select
from src.database.models import PetRead, Pet


def get_all_pets(session: Session) -> list[PetRead]:
    return session.exec(select(Pet)).all()


def pet_by_id(pet_id: int, session: Session) -> PetRead | None:
    return session.get(Pet, pet_id)
