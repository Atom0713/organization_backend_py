from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from .controller import check_credentials
from ..utils import logger

bp = Blueprint("auth", __name__, url_prefix="/login")


@bp.route("/", methods=["POST"])
def handle_login():
    user_id = check_credentials()
    if not user_id:
        logger.warning(f"User  `{request.json.get('username')}` not found.")
        return {"msg": "Bad username or password"}, 401
    
    access_token = create_access_token(identity=user_id)
    return jsonify(access_token=access_token), 200
