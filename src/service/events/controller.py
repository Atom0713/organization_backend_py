from .queries import get_events_paginated


def resolve_get_events():
    return [event.tod_dict() for event in get_events_paginated()]


def resolve_get_event(id):
    return {
        "id": id,
        "name": "Event 4",
        "date": "20/20/1020",
        "description": "Ride till we gotta go home.",
    }


def resolve_post_events():
    return {
        "status": "success",
        "data": {
            "id": 5,
            "name": "Event 5",
            "description": "eat cock",
            "date": "2022-09-09T19:00:00+00:00",
            "location": "Up your ass!",
        },
    }


def resolve_get_event_attendance(id):
    return {
        "id": id,
        "expected": 100,
        "attended": 50,
    }


def resolve_post_event_attendance(id):
    return {"status": "success", "id": 5}
