from flask import Blueprint

from ..utils import handle_response
from .controller import resolve_get_user_permissions

bp = Blueprint("role", __name__, url_prefix="/role")


@bp.route("/user_id/<id>", methods=["GET"])
@handle_response
def get_user_permissions(id):
    return resolve_get_user_permissions(id)
