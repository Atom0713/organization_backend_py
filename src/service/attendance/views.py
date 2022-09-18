from flask import Blueprint, request

from ..constants import HTTPRequestMethods
from .controller import resolve_post_attendance

bp = Blueprint("attendance", __name__, url_prefix="/attendance")


@bp.route("/", methods=["GET", "POST"])
def handle_attendance():
    if request.method == HTTPRequestMethods.POST:
        return resolve_post_attendance()
