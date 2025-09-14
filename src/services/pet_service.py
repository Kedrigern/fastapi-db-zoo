from sqlmodel import Session, select
from src.database.models import Pet
from src.services.kind_service import kind_by_id


def pets_all(session: Session) -> list[Pet]:
    return session.exec(select(Pet)).all()


def pet_by_id(pet_id: int, session: Session) -> Pet | None:
    return session.get(Pet, pet_id)


def pet_add(pet: Pet, session: Session) -> Pet:
    if kind_by_id(pet.kind_id, session) is None:
        raise ValueError(f"Kind not found (id {pet.kind_id})")
    session.add(pet)
    session.commit()
    session.refresh(pet)
    return pet