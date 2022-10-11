from flask import Blueprint
from flask_jwt_extended import jwt_required

from ..utils import handle_response, logger
from .controller import (resolve_add_user, resolve_get_user_by_id,
                         resolve_get_users_by_role)

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/", methods=["GET"])
@jwt_required()
@handle_response
def get_user_by_id():
    return resolve_get_user_by_id()


@bp.route("/role/<role_id>/", methods=["GET"])
@jwt_required()
@handle_response
def get_users_by_role(role_id):

    return resolve_get_users_by_role(role_id)


@bp.route("/add", methods=["POST"])
@jwt_required()
@handle_response
def add_user():
    email = resolve_add_user()
    logger.info(f"Added new user. Username: {email}")
    return {"username": email}
