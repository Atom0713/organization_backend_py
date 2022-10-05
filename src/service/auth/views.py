from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

bp = Blueprint("auth", __name__, url_prefix="/login")


@bp.route("/", methods=["POST"])
def handle_login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"msg": "Bad username or password"}), 401
    user_id = 123456789
    access_token = create_access_token(identity=user_id)
    return jsonify(access_token=access_token)
