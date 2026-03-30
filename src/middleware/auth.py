from functools import wraps
from flask import request, jsonify, current_app
import jwt
from src.utils.security import verify_password
from src.models import User  # Assuming you have a User model

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({'message': 'Token is missing'}), 401

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            user = User.query.filter_by(public_id=data['public_id']).first()
            if user is None:
                return jsonify({'message': 'Invalid Token'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        except Exception as e:
            print(e)
            return jsonify({'message': 'Invalid token'}), 401

        return f(user, *args, **kwargs)

    return decorated

def authenticate(username, password):
    """
    Authenticates a user based on username and password.
    Returns a user object if authentication is successful, None otherwise.
    """
    user = User.query.filter_by(username=username).first()
    if user and verify_password(password, user.password):
        return user
    return None

def generate_token(user):
    """
    Generates a JWT token for the given user.
    """
    token = jwt.encode({
        'public_id': user.public_id,
        'exp': current_app.config['JWT_EXPIRATION_DELTA']
    }, current_app.config['SECRET_KEY'], algorithm="HS256")
    return token