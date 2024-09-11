from flask import Blueprint, request, jsonify
from .models import Users, database

api_routes = Blueprint('api', __name__)

# Get all user
@api_routes.route('users', methods=['GET'])
def get_users():
    users = Users.query.all()
    return jsonify([{'id': user.id, 'user_id': user.user_id, 'username': user.username, 'password': user.password, 'email': user.email, 'phone': user.phone} for user in users])

# Create a new user
@api_routes.route('users', methods=['POST'])
def create_user():
    data = request.get_json()

    new_user = Users(user_id = data['user_id'], username = data['username'], password=data['password'], email = data['email'], phone = data['phone'])
    database.session.add(new_user)
    database.session.commit()

    return jsonify({'message' : 'User created successfully'}), 201

# Update a user
@api_routes.route('users/<int:id>', methods=['PUT'])
def update_user(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    data = request.get_json()
    
    user.email = data.get('email', user.email)
    user.phone = data.get('phone', user.phone)

    database.session.commit()

    return jsonify({'message' : 'User updated successfully'}), 200

# Delete a user
@api_routes.route('users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    database.session.delete(user)
    database.session.commit()

    return jsonify({'message': 'User deleted successfully'}), 200
    