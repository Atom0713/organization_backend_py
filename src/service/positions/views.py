from flask import Blueprint
from flask_jwt_extended import jwt_required

from ..utils import handle_response
from .controller import get_all_positions

bp = Blueprint("positions", __name__, url_prefix="/positions")


@bp.route("/", strict_slashes=False, methods=["GET"])
@jwt_required()
@handle_response
def handle_get_positions():
    return get_all_positions()
