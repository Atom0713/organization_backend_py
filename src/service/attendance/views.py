from flask import Blueprint
from .controller import resolve_post_attendance

bp = Blueprint("attendance", __name__, url_prefix="/attendance")

@bp.route("/", methods=['GET', "POST"])
def handle_attendance():
    return resolve_post_attendance()