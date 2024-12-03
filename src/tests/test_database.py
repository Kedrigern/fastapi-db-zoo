from datetime import datetime
from sqlmodel import Session
from src.database.models import Pet, Kind
from src.services.pet_service import get_all_pets


def prepare_data(session: Session):
    franchie = Kind(
        name="French buldock"
    )
    session.add(franchie)
    session.add(Kind(
        name="Boxer"
    ))
    session.add(Kind(
        name="Persian cat"
    ))
    session.commit()
    session.refresh(franchie)
    session.add(Pet(
        name="Arya",
        born=datetime.fromisoformat("2023-06-15"),
        kind_id=franchie.id
    ))
    session.commit()


def test_db_prep(session: Session):
    assert get_all_pets(session) == []
    prepare_data(session)
    pets = get_all_pets(session)
    assert pets is not None
    assert len(pets) == 1


def test_get_pet(session: Session):
    prepare_data(session)
    pets = get_all_pets(session)
    assert pets[0].name == "Arya"
    assert pets[0].kind.name == "French buldock"