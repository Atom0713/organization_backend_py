from flask import Blueprint, jsonify

bp = Blueprint("common", __name__)


@bp.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})
