from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__, url_prefix="/v1/auth")


@auth_bp.route('register', methods = ['POST'])
def register():
    