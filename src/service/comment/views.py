from flask import Blueprint, request

from src.service.constants import HTTPRequestMethods

from .controller import resolve_add_comments, resolve_get_comments

bp = Blueprint("comment", __name__, url_prefix="/comment")


@bp.route("/", methods=["GET", "POST"])
def handle_comment():
    if request.method == HTTPRequestMethods.GET:
        return resolve_get_comments()

    if request.method == HTTPRequestMethods.POST:
        return resolve_add_comments()
