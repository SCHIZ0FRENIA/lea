from flask import Blueprint, request, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['POST'])
def create_user_route():
    data = request.get_json()

    if not data:
        return jsonify({"error", "invalid Json"}), 400
