from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from ..utils import handle_response, HTTPRequestMethods
from .controller import (resolve_get_event, resolve_get_event_attendance,
                         resolve_get_events, resolve_post_event,
                         resolve_post_event_attendance, resolve_get_event_attendance)

bp = Blueprint("events", __name__, url_prefix="/event")


@bp.route("/", methods=["GET", "POST"])
@jwt_required()
@handle_response
def handle_events():
    if request.method == HTTPRequestMethods.GET:
        return resolve_get_events()

    if request.method == HTTPRequestMethods.POST:
        return resolve_post_event()


@bp.route("/<event_id>/", methods=["GET"])
@jwt_required()
@handle_response
def get_event_by_id(event_id):
    return resolve_get_event(event_id)


@bp.route("/attendance/", methods=["POST"])
@jwt_required()
@handle_response
def add_attendance():
    return resolve_post_event_attendance()


@bp.route("/attendance/<event_id>/", methods=["GET"])
@jwt_required()
@handle_response
def add_attendance_by_event(event_id: int):
    return {"data": resolve_get_event_attendance(event_id)}