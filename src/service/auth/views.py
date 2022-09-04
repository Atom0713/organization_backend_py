from flask import Blueprint, jsonify, request

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["POST"])
def graphql_server():
    data = request.get_json()
    print(data)

    return jsonify({"token": "dkljfgweyofhiu3nnqr"})
