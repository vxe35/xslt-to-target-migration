import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models import User  # Import your User model
from src import create_app  # Import your app factory function
from src.utils.security import get_password_hash
import os

@pytest.fixture(scope="session")
def app():
    """
    Creates a Flask application instance for testing.
    """
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',  # Use an in-memory SQLite database for testing
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SECRET_KEY': 'test_secret_key',  # Replace with a strong secret key for testing
        'JWT_EXPIRATION_DELTA': 3600
    })

    with app.app_context():
        db = SQLAlchemy(app)
        db.create_all()

        # Create a test user
        hashed_password = get_password_hash("test_password")
        test_user = User(username="test_user", password=hashed_password, public_id="test_public_id")
        db.session.add(test_user)
        db.session.commit()

        yield app

        db.session.remove()
        db.drop_all()

@pytest.fixture(scope="session")
def client(app):
    """
    Creates a Flask test client using the application fixture.
    """
    return app.test_client()

@pytest.fixture(scope="session")
def db(app):
    """
    Returns the SQLAlchemy database instance.
    """
    return SQLAlchemy(app)