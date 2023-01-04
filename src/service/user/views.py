from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from ..utils import handle_response, logger, HTTPRequestMethods
from .controller import (resolve_add_user, resolve_get_user_by_id, resolve_get_user,
                         resolve_get_users_by_role)

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/", methods=["GET", "POST"])
@jwt_required()
@handle_response
def handle_user():

    if request.method == HTTPRequestMethods.GET:
        return resolve_get_user()

    if request.method == HTTPRequestMethods.POST:
        return resolve_add_user()
    return 


@bp.route("/<user_id>", methods=["GET"])
@jwt_required()
@handle_response
def get_user_by_id(user_id):
    return resolve_get_user_by_id(user_id)


@bp.route("/role/<role_id>/", methods=["GET"])
@jwt_required()
@handle_response
def get_users_by_role(role_id):

    return resolve_get_users_by_role(role_id)
