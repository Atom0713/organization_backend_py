from flask import Blueprint
from .controller import resolve_get_events, resolve_get_event

bp = Blueprint("events", __name__, url_prefix="/event")

@bp.route("/")
def get_events():
    return resolve_get_events()

@bp.route("/<event_id>/")
def get_event_by_id(event_id):
    return resolve_get_event(event_id)
