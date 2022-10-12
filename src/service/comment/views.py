from flask import Blueprint
from flask_jwt_extended import jwt_required

from ..utils import handle_response
from .controller import resolve_get_event_comments, resolve_post_comment

bp = Blueprint("comment", __name__, url_prefix="/comment")


@bp.route("/add", methods=["POST"])
@jwt_required()
@handle_response
def handle_post_comment():
    return resolve_post_comment()


@bp.route("/event/<event_id>", methods=["GET"])
@jwt_required()
@handle_response
def get_event_comments(event_id):
    return resolve_get_event_comments(event_id)
