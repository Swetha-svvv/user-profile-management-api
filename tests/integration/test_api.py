from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health():

    response = client.get("/health")

    assert response.status_code == 200


def test_root():

    response = client.get("/")

    assert response.status_code == 200


def test_create_get_update_delete_user():

    # Create

    response = client.post(
        "/api/users",
        json={
            "name": "Integration User",
            "email": "integration@example.com"
        }
    )

    assert response.status_code == 201

    user = response.json()

    user_id = user["id"]

    # Get

    response = client.get(f"/api/users/{user_id}")

    assert response.status_code == 200

    # Update

    response = client.put(
        f"/api/users/{user_id}",
        json={
            "name": "Updated Integration User",
            "email": "integration@example.com"
        }
    )

    assert response.status_code == 200

    # Enriched

    response = client.get(f"/api/users/{user_id}/enriched")

    assert response.status_code == 200

    # Delete

    response = client.delete(f"/api/users/{user_id}")

    assert response.status_code == 204