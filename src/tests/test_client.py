from fastapi.testclient import TestClient
from sqlmodel import Session
from .test_database import prepare_data


def test_bad_url(client: TestClient):
    response = client.get('/abc')
    assert response.status_code == 404


def test_pet_list_empty(client: TestClient):
    response = client.get('/pet')
    assert response.status_code == 200
    assert list(response.json()) == []


def test_pet_list(client: TestClient, session: Session):
    prepare_data(session)
    response = client.get('/pet')
    assert response.status_code == 200
    assert len(response.json()) == 1