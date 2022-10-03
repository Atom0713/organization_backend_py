from datetime import datetime


def resolve_get_events():
    return {
        "events": [
            {
                "id": 1,
                "name": "Event 1",
                "date": "20/20/1020",
                "description": "Ride till we gotta go home.",
            },
            {
                "id": 2,
                "name": "Event 2",
                "date": "20/20/1020",
                "description": "Ride till we gotta go home.",
            },
            {
                "id": 3,
                "name": "Event 3",
                "date": "20/20/1020",
                "description": "Ride till we gotta go home.",
            },
            {
                "id": 4,
                "name": "Event 4",
                "date": "20/20/1020",
                "description": "Ride till we gotta go home.",
            },
        ]
    }


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
