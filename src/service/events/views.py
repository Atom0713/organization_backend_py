from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from ..constants import HTTPRequestMethods
from ..utils import handle_response
from .controller import (
    resolve_get_event,
    resolve_get_event_attendance,
    resolve_get_events,
    resolve_post_event_attendance,
    resolve_post_events,
)

bp = Blueprint("events", __name__, url_prefix="/event")


@bp.route("/", methods=["GET", "POST"])
@jwt_required()
@handle_response
def handle_events():
    if request.method == HTTPRequestMethods.GET:
        return resolve_get_events()

    if request.method == HTTPRequestMethods.POST:
        return resolve_post_events()


@bp.route("/<event_id>/", methods=["GET"])
@jwt_required()
@handle_response
def get_event_by_id(event_id):
    return resolve_get_event(event_id)


@bp.route("/attendance/<id>/", methods=["GET", "POST"])
@jwt_required()
@handle_response
def add_attendance(id):
    if request.method == HTTPRequestMethods.GET:
        return resolve_get_event_attendance(id)

    if request.method == HTTPRequestMethods.POST:
        return resolve_post_event_attendance(id)
