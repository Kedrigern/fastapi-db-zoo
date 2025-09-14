from sqlmodel import Session
from src.database.connection import fill_demo_data
from src.services.pet_service import pets_all, pet_by_id
from src.services.kind_service import kind_all, kind_by_id

def prepare_data(session: Session):
    fill_demo_data(session)


def test_db_prep(session: Session):
    assert pets_all(session) == []
    prepare_data(session)
    pets = pets_all(session)
    assert pets is not None
    assert len(pets) == 2


def test_kind_service_list(session: Session):
    assert len(kind_all(session)) == 0
    prepare_data(session)
    kinds = kind_all(session)
    assert len(kinds) == 3
    assert kinds[0].name == "French Bulldog"
    assert kinds[1].name == "Boxer"
    assert kinds[2].name == "Persian cat"
    kind = kind_by_id(1, session)
    assert kind.name == "French Bulldog"

def test_pet_service_list(session: Session):
    assert len(pets_all(session)) == 0
    prepare_data(session)
    pets = pets_all(session)
    assert len(pets) == 2
    assert pets[0].name == "Arya"
    assert pets[0].kind.name == "French Bulldog"
    assert pets[1].name == "Bruno"
    assert pets[1].kind.name == "Boxer"
    pet = pet_by_id(1, session)
    assert pet.name == "Arya"
    assert pet.kind.name == "French Bulldog"