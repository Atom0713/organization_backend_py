from src.models import Event
from typing import List
from src.datastore import commit_to_db


def get_events_paginated() -> List[Event]:
    return Event.get_all()


def insert_event(attributes: dict) -> "Event":
    new_event = Event(**attributes)
    commit_to_db(new_event)
    return new_event


def query_event(event_id: int) -> "Event":
    return Event.get(event_id)