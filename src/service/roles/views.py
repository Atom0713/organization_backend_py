from flask import Blueprint
from .controller import resolve_get_user_permissions

bp = Blueprint("role", __name__, url_prefix="/role")


@bp.route("/user_id/<id>", methods=["GET"])
def get_user_permissions(id):
    return resolve_get_user_permissions(id)