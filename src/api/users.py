from flask import Blueprint, jsonify, request
from src.database import db

users_bp = Blueprint('users', __name__, url_prefix='/api/users')

@users_bp.route('/', methods=['GET'])
def list_users():
    # Placeholder for fetching users from the database
    users = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}] # Replace with actual database query
    return jsonify(users)

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Placeholder for fetching a specific user from the database
    user = {"id": user_id, "name": f"User {user_id}"} # Replace with actual database query
    return jsonify(user)

@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    # Placeholder for creating a new user in the database
    # Example:
    # new_user = User(name=data['name'], email=data['email'])
    # db.session.add(new_user)
    # db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    # Placeholder for updating a user in the database
    # Example:
    # user = User.query.get(user_id)
    # user.name = data['name']
    # db.session.commit()
    return jsonify({"message": f"User {user_id} updated successfully"})

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Placeholder for deleting a user from the database
    # Example:
    # user = User.query.get(user_id)
    # db.session.delete(user)
    # db.session.commit()
    return jsonify({"message": f"User {user_id} deleted successfully"})