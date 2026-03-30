import pytest
import json

def test_get_all_users(client, db):
    """
    Tests the endpoint to retrieve all users.
    """
    # Assuming you have a test user created in the conftest.py fixture
    response = client.get("/users")
    assert response.status_code == 200
    users = json.loads(response.data.decode("utf-8"))
    assert isinstance(users, list)
    assert len(users) > 0  # Assuming there's at least one test user
    assert "username" in users[0]
    assert "public_id" in users[0]
    assert "password" not in users[0]  # Ensure password is not returned

def test_get_user_by_id(client, db):
    """
    Tests the endpoint to retrieve a user by ID.
    """
    # Assuming you have a test user created in the conftest.py fixture
    response = client.get("/users/test_public_id")  # Replace with the actual public_id of the test user
    assert response.status_code == 200
    user = json.loads(response.data.decode("utf-8"))
    assert user["username"] == "test_user"  # Replace with the actual username of the test user
    assert user["public_id"] == "test_public_id"  # Replace with the actual public_id of the test user
    assert "password" not in user  # Ensure password is not returned

def test_get_user_by_id_not_found(client, db):
    """
    Tests the endpoint to retrieve a user by ID when the user is not found.
    """
    response = client.get("/users/non_existent_id")
    assert response.status_code == 404
    response_data = json.loads(response.data.decode("utf-8"))
    assert "message" in response_data
    assert response_data["message"] == "User not found"