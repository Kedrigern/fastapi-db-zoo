from sqlmodel import Session
from src.database.connection import fill_demo_data
from src.services.pet_service import get_all_pets


def prepare_data(session: Session):
    fill_demo_data(session)


def test_db_prep(session: Session):
    assert get_all_pets(session) == []
    prepare_data(session)
    pets = get_all_pets(session)
    assert pets is not None
    assert len(pets) == 2


def test_get_pet(session: Session):
    prepare_data(session)
    pets = get_all_pets(session)
    assert pets[0].name == "Arya"
    assert pets[0].kind.name == "French Bulldog"
