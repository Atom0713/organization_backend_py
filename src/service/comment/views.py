from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from src.service.constants import HTTPRequestMethods

from ..utils import handle_response
from .controller import resolve_get_comments, resolve_post_comment

bp = Blueprint("comment", __name__, url_prefix="/comment")


@bp.route("/", methods=["GET", "POST"])
@jwt_required()
@handle_response
def handle_comment():
    if request.method == HTTPRequestMethods.GET:
        return resolve_get_comments()

    if request.method == HTTPRequestMethods.POST:
        return resolve_post_comment()
