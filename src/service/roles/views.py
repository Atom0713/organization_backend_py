from flask import Blueprint
from flask_jwt_extended import jwt_required

from ..utils import handle_response
from .controller import resolve_get_all_user_roles, resolve_get_user_permissions

bp = Blueprint("role", __name__, url_prefix="/role")


@bp.route("/", methods=["GET"])
@jwt_required()
@handle_response
def get_all_roles():
    return {"data": resolve_get_all_user_roles()}


@bp.route("/user_id/<user_id>", methods=["GET"])
@jwt_required()
@handle_response
def get_user_permissions(user_id):
    return resolve_get_user_permissions(user_id)
