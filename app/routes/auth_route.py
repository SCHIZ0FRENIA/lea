from flask import Blueprint, request, jsonify, current_app
from pydantic import ValidationError
from pymongo.errors import DuplicateKeyError
from werkzeug.exceptions import BadRequest

from ..schemas.user_schema import UserCreate, UserLogin
from ..static.services import Services
from ..utils.exceptions.database_exception import DatabaseException

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_auth_route():
    user_service = current_app.services[Services.USER_SERVICE]
    try:
        data = request.get_json()
        if data is None:
            raise BadRequest("Invalid JSON")

        user_data = UserCreate(**data)

        try:
            result = user_service.create_user(
                user_data.name,
                user_data.password,
                user_data.role
            )
        except DuplicateKeyError as e:
            current_app.logger.error(f"Duplicate user error: {str(e)}")
            return jsonify({"message": "Username already exists."}), 409

        return jsonify({
            "id": str(result.inserted_id),
            "name": user_data.name,
            "role": user_data.role
        }), 201

    except BadRequest as e:
        return jsonify({"message": "Invalid JSON provided."}), 400
    except ValidationError as e:
        errors = e.errors()
        current_app.logger.warning(f"Validation error: {errors}")
        return jsonify({"message": "Invalid user data provided."}), 400
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"message": "Internal server error."}), 500

@auth_bp.route('/login', methods=['POST'])
def login_auth_route():
    user_service = current_app.services[Services.USER_SERVICE]
    try:
        data = request.get_json()

        if data is None:
            raise BadRequest("Invalid JSON.")

        user_data = UserLogin(**data)

        try:
            result = user_service.check_user(user_data.name, user_data.password)
        except DatabaseException as e:
            return jsonify({
                "message": str(e)
            }), 400


        if result is not None:
            return jsonify({
                "role": result["role"],
                "message": str(result)
            }), 200
        else:
            return jsonify({
                "message": "Provided password is incorrect!"
            }), 401

    except BadRequest as e:
        return jsonify({"message": "Invalid JSON provided."}), 400
    except ValidationError as e:
        errors = e.errors()
        current_app.logger.warning(f"Validation error: {errors}")
        return jsonify({"message": "Invalid user data provided."}), 400
    except Exception as e:
        current_app.logger.error(f"Error: {str(e)}")
        return jsonify({"message": "Internal server error."}), 500