from flask import Blueprint, request
from .controller import resolve_get_events, resolve_get_event, resolve_post_events
from ..constants import HTTPRequestMethods

bp = Blueprint("events", __name__, url_prefix="/event")


@bp.route("/", methods=['GET', 'POST'])
def handle_events():
    if request.method == HTTPRequestMethods.GET:
        return resolve_get_events()

    if request.method == HTTPRequestMethods.POST:
        return resolve_post_events()

@bp.route("/<event_id>/")
def get_event_by_id(event_id):
    return resolve_get_event(event_id)