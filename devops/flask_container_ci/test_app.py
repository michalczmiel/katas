import pytest

from app.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_main_page(client):
    response = client.get("/", follow_redirects=True)
    data = response.json
    assert response.status_code == 200
    assert data["current_uri"] == "/"
    assert data["resources_uris"]["user"]
    assert data["resources_uris"]["users"]


def test_users_page(client):
    response = client.get("/users", follow_redirects=True)
    assert response.status_code == 200
    assert len(response.json) == 4


def test_specific_user(client):
    geralt = {
        "description": "Traveling monster slayer for hire",
        "name": "Geralt of Rivia",
    }

    response = client.get("/users/geralt", follow_redirects=True)
    assert response.status_code == 200
    assert response.json == geralt


def test_health_page(client):
    response = client.get("/health", follow_redirects=True)
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
