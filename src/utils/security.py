import hashlib
import secrets
import os

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def generate_random_secret_key(length=32):
    """Generates a random secret key."""
    return secrets.token_urlsafe(length)

def generate_salt():
    """Generates a random salt for password hashing."""
    return os.urandom(16).hex()

def hash_password_with_salt(password, salt):
    """Hashes a password with a salt using SHA-256."""
    salted_password = salt + password
    hashed_password = hashlib.sha256(salted_password.encode('utf-8')).hexdigest()
    return hashed_password