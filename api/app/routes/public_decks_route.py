from flask import current_app, jsonify, request, Blueprint
from pydantic import ValidationError
from werkzeug.exceptions import BadRequest

from ..schemas.deck_schema import Deck
from ..static.services import Services
from ..utils.exceptions.lea_exception import LeaException

public_decks_bp = Blueprint('public_decks_bp', __name__)

@public_decks_bp.route('/', methods=['POST'])
def create_public_deck_route():
    decks_service = current_app.services[Services.PUBLIC_DECKS_SERVICE]

    try:
        data = request.get_json()
        if data is None:
            raise BadRequest("Invalid JSON")

        deck = Deck(**data)

        decks_service.create_public_deck(deck)

        return jsonify({"message": "Deck successfully created"}), 201

    except ValidationError as e:
        errors = e.errors()
        current_app.logger.warning(f"Validation error: {errors}")
        return jsonify({"message": "Invalid user data"}), 400
    except LeaException as e:
        current_app.logger.warning(f"Public deck creation error: {str(e)}")
        return jsonify({"message": str(e)}), 400
    except BadRequest as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        current_app.logger.warning(f"Internal server error: {str(e)}")
        return jsonify({"message": str(e)}), 500