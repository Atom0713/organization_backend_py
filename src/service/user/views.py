from flask import Blueprint, jsonify, request

from .controller import (
    resolve_add_user,
    resolve_get_all_user_roles,
    resolve_get_users_by_role,
)

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/<id>", methods=["GET"])
def get_user_by_id(id):

    return jsonify({"name": "Artem Sliusarenko", "id": 1})


@bp.route("/role/<role_id>/", methods=["GET"])
def get_users_by_role(role_id):

    return resolve_get_users_by_role(role_id)


@bp.route("/roles", methods=["GET"])
def get_all_user_roles():

    return resolve_get_all_user_roles()


@bp.route("/add", methods=["POST"])
def add_user():

    return resolve_add_user()
