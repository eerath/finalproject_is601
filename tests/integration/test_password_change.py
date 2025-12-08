# tests/integration/test_password_change.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.user import User
from uuid import uuid4

client = TestClient(app)

def register_user(client, payload):
    return client.post("/auth/register", json=payload)

def login_user(client, payload):
    return client.post("/auth/login", json=payload)

@pytest.fixture
def test_user(db_session):
    # create user via register route so tokens match app logic
    payload = {
        "first_name": "Test",
        "last_name": "User",
        "email": "testpw@example.com",
        "username": "testpwuser",
        "password": "OldPass123!",
        "confirm_password": "OldPass123!"
    }
    r = register_user(client, payload)
    assert r.status_code == 201
    return payload

def get_auth_header(client, username, password):
    r = login_user(client, {"username": username, "password": password})
    assert r.status_code == 200
    data = r.json()
    token = data["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_change_password_flow(db_session, test_user):
    # login with old password
    headers = get_auth_header(client, test_user["username"], "OldPass123!")

    # change password
    payload = {
        "current_password": "OldPass123!",
        "new_password": "NewPass123!",
        "confirm_new_password": "NewPass123!"
    }
    r = client.put("/users/me/password", json=payload, headers=headers)
    assert r.status_code == 200

    # attempt login with old password (should fail)
    r_old = login_user(client, {"username": test_user["username"], "password": "OldPass123!"})
    assert r_old.status_code == 401

    # login with new password (should succeed)
    r_new = login_user(client, {"username": test_user["username"], "password": "NewPass123!"})
    assert r_new.status_code == 200
