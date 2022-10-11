from typing import List

from src.models import Event


def get_events_paginated() -> List[Event]:
    return Event.get_all()
