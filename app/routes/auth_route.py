from flask import Blueprint, request, jsonify, current_app
from werkzeug.exceptions import BadRequest
from flask_jwt_extended import create_access_token

from ..schemas.user_schema import UserCreate, UserLogin
from ..static.services import Services

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_auth_route():
    print(request.json)
    user_service = current_app.services[Services.USER_SERVICE]
    data = request.get_json()
    if data is None:
        raise BadRequest("Invalid JSON provided.")

    user_data = UserCreate(**data)

    result = user_service.create_user(
        user_data.login,
        user_data.password,
        user_data.role
    )
    access_token = create_access_token(
        identity={
            "user_id": str(result.inserted_id),
            "login": user_data.login,
            "role": user_data.role.value
        }
    )

    return jsonify({
        "message": "User registered successfully.",
        "token": access_token,
        "role": user_data.role.value
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login_auth_route():
    user_service = current_app.services[Services.USER_SERVICE]
    data = request.get_json()

    if data is None:
        raise BadRequest("Invalid JSON provided.")

    user_data = UserLogin(**data)

    result = user_service.check_user(user_data.login, user_data.password)
    access_token = create_access_token(
        identity={
            "user_id": str(result["_id"]),
            "login": result["login"],
            "role": result["role"]
        }
    )

    return jsonify({
        "message": "Login successful.",
        "token": access_token,
        "role": result["role"]
    }), 200
