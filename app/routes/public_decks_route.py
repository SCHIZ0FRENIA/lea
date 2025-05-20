from flask import current_app, jsonify, request, Blueprint
from werkzeug.exceptions import BadRequest

from ..schemas.deck_schema import Deck
from ..static.services import Services

public_decks_bp = Blueprint('public_decks_bp', __name__)

@public_decks_bp.route('/', methods=['POST'])
def create_public_deck_route():
    decks_service = current_app.services[Services.PUBLIC_DECKS_SERVICE]

    data = request.get_json()
    if data is None:
        raise BadRequest("Invalid JSON provided.")

    deck = Deck(**data)

    decks_service.create_public_deck(deck)

    return jsonify({"message": "Deck successfully created"}), 201
