from flask import Blueprint, request, jsonify, current_app
from pydantic import ValidationError
from pymongo.errors import DuplicateKeyError
from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash

from ..extensions import mongo
from ..schemas.user_schema import UserCreate

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['POST'])
def create_user_route():
    try:
        data = request.get_json()
        if data is None:
            raise BadRequest("Invalid JSON")

        user_data = UserCreate(**data)

        hashed_password = generate_password_hash(
            user_data.password,
            method='pbkdf2:sha256'
        )

        try:
            result = mongo.db.users.insert_one({
                "name": user_data.name,
                "password": hashed_password,
                "role": user_data.role
            })
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
