from flask import Blueprint, request

from .token import encode_auth_token

bp = Blueprint("auth", __name__, url_prefix="/login")


@bp.route("/", methods=["POST"])
def handle_login():
    # data = request.get_json()
    user_id = 1
    return {"token": encode_auth_token(user_id)}
