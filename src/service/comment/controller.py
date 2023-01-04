from typing import Dict, List

from flask import request

from ..queries import insert_comment, query_event_comments


def resolve_get_event_comments(event_id: int) -> List[Dict]:
    return [comment.to_dict() for comment in query_event_comments(event_id)]


def resolve_post_comment():
    attributes = {
        "comment": request.json.get("comment"),
        "user_id": request.json.get("user_id"),
        "event_id": request.json.get("event_id"),
    }

    new_comment = insert_comment(attributes)
    return new_comment.to_dict()
