from flask import Blueprint, jsonify
from flask_cors import cross_origin

bp = Blueprint("common", __name__)


@bp.route("/", methods=["GET"])
@cross_origin()
def health_check():
    return jsonify({"status": "ok"})
