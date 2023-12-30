from typing import List

from src.datastore import commit_to_db
from src.models import Attendance, Event, User


def insert_attendance(attendance: List, event_id: int) -> None:
    event = Event.get(event_id)
    collection = []
    for user_id, player_attendance in attendance.items():
        user = User.get(user_id)
        collection.append(Attendance(**player_attendance, user=user, event=event))

    commit_to_db(collection, multiple=True)
    event.completed = True
    commit_to_db(event)


def query_event_attendance_by_event_id(event_id: int) -> List["Attendance"]:
    return Attendance.query.filter(Attendance.event_id == event_id).all()
