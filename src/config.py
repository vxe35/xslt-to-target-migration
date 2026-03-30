import os

class Config:
    PORT = int(os.environ.get("PORT", 8080))
    SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key")
    # Add other configuration variables here