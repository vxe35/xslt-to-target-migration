import pytest
import json
from src.utils.security import verify_password
from src.models import User

def test_register(client, db):
    """
    Tests the user registration endpoint.
    """
    data = {
        "username": "new_user",
        "password": "new_password"
    }
    response = client.post("/register", json=data)
    assert response.status_code == 201
    response_data = json.loads(response.data.decode("utf-8"))
    assert "message" in response_data
    assert response_data["message"] == "Registered successfully."

    # Verify that the user was created in the database
    with client.application.app_context():
        user = User.query.filter_by(username="new_user").first()
        assert user is not None
        assert verify_password("new_password", user.password)

def test_login(client, db):
    """
    Tests the user login endpoint.
    """
    data = {
        "username": "test_user",
        "password": "test_password"
    }
    response = client.post("/login", json=data)
    assert response.status_code == 200
    response_data = json.loads(response.data.decode("utf-8"))
    assert "token" in response_data

def test_login_invalid_credentials(client, db):
    """
    Tests the user login endpoint with invalid credentials.
    """
    data = {
        "username": "test_user",
        "password": "wrong_password"
    }
    response = client.post("/login", json=data)
    assert response.status_code == 401
    response_data = json.loads(response.data.decode("utf-8"))
    assert "message" in response_data
    assert response_data["message"] == "Invalid credentials"