from fastapi.testclient import TestClient
from sqlmodel import Session
from .test_database import prepare_data


def test_bad_url(client: TestClient):
    response = client.get("/abc")
    assert response.status_code == 404


def test_welcome(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello world" in response.json()["detail"]


def test_pet_list_empty(client: TestClient):
    response = client.get("/pet")
    assert response.status_code == 200
    assert list(response.json()) == []


def test_pet_list(client: TestClient, session: Session):
    prepare_data(session)
    response = client.get("/pet")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_pet(client: TestClient, session: Session):
    response = client.get("/pet/1")
    assert response.status_code == 404
    prepare_data(session)
    response = client.get("/pet/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Arya"


def test_get_kind(client: TestClient, session: Session):
    response = client.get("/kind/1")
    assert response.status_code == 404
    prepare_data(session)
    response = client.get("/kind/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "French buldock"
