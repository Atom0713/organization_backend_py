from typing import Dict
from src.service.queries import get_events_paginated, insert_event, query_event
from flask import request

from ..utils import DATE_FORMAT, logger
from datetime import datetime


def resolve_get_events():
    return [event.to_dict(show_additional=False) for event in get_events_paginated()]


def resolve_get_event(event_id: int) -> Dict:
    return query_event(event_id).to_dict()


def resolve_post_event():
    attributes = {
        "name": request.json.get("name"),
        "description": request.json.get("description"),
        "date": datetime.strptime(request.json.get("date"), DATE_FORMAT),
        "location": request.json.get("location"),
    }

    new_event = insert_event(attributes)
    logger.info(f"Created new event `{new_event.name}`.")

    return {
            "id": new_event.id,
            "name": new_event.name,
            "description": new_event.description,
            "date": new_event.date,
            "location": new_event.location,
        }


def resolve_get_event_attendance(id):
    return {
        "id": id,
        "expected": 100,
        "attended": 50,
    }


def resolve_post_event_attendance(id):
    return {"status": "success", "id": 5}
