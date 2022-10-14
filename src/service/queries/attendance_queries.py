from typing import Dict, List

from src.datastore import commit_to_db
from src.models import Attendance, Event, User


def insert_attendance(attributes: Dict, event_id: int) -> None:
    event = Event.get(event_id)
    for user_id, attendance_stats in attributes.items():
        user = User.get(user_id)
        new_attendance = Attendance(**attendance_stats, user=user, event=event)
        commit_to_db(new_attendance)
    event.completed = True
    commit_to_db(event)


def query_event_attendance_by_event_id(event_id: int) -> List["Attendance"]:
    return Attendance.query.filter(Attendance.event_id == event_id).all()
