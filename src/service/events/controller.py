from datetime import datetime
from typing import Dict

from flask import request

from src.service.queries import (
    get_events_paginated,
    insert_attendance,
    insert_event,
    query_event,
    query_event_attendance_by_event_id,
)

from ..utils import DATETIME_FORMAT, logger


def resolve_get_events():
    return [event.to_dict() for event in get_events_paginated()]


def resolve_get_event(event_id: int) -> Dict:
    return query_event(event_id).to_dict()


def resolve_post_event():
    attributes = {
        "name": request.json.get("name"),
        "description": request.json.get("description"),
        "date": datetime.strptime(request.json.get("date"), DATETIME_FORMAT),
        "location": request.json.get("location"),
    }

    new_event = insert_event(attributes)
    logger.info(f"Created new event `{new_event.name}`.")

    return new_event.to_dict()


def resolve_post_event_attendance() -> Dict:
    event_id = request.json.get("event_id")
    attendance = request.json.get("attendance")

    insert_attendance(attendance, event_id)
    return {"event_id": event_id}


def resolve_get_event_attendance(event_id: int) -> Dict:
    event_attendance = query_event_attendance_by_event_id(event_id)
    return [attendie.to_dict() for attendie in event_attendance]
