from flask import Blueprint, request, jsonify
from ..database.database import instance

auth_bp = Blueprint('auth', __name__, url_prefix="/v1/auth")


@auth_bp.route('register', methods = ['POST'])
def register():
    data = request.get_json()

    if instance.addUser(data['name'], data['password']):
        return jsonify({'message': 'User created succesfully'}), 201
    else:
        return jsonify({'message' : 'Username is already in use'}), 409