from flask import Blueprint, jsonify, request

from ..utils import handle_response
from .controller import (resolve_add_user, resolve_get_all_user_roles,
                         resolve_get_users_by_role)

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/", methods=["GET"])
@handle_response
def get_user_by_id():

    return {
            "name": "Artem Sliusarenko",
            "id": 1,
            "role": "Staff",
            "date": "2022-09-09",
    }


@bp.route("/role/<role_id>/", methods=["GET"])
@handle_response
def get_users_by_role(role_id):

    return resolve_get_users_by_role(role_id)


@bp.route("/roles", methods=["GET"])
@handle_response
def get_all_user_roles():

    return resolve_get_all_user_roles()


@bp.route("/add", methods=["POST"])
@handle_response
def add_user():

    return resolve_add_user()
