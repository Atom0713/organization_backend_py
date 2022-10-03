from flask import Blueprint, request

from ..utils import handle_response

bp = Blueprint("auth", __name__, url_prefix="/login")


@bp.route("/", methods=["POST"])
@handle_response
def handle_login():
    data = request.get_json()

    return {"token": "dkljfgweyofhiu3nnqr"}
