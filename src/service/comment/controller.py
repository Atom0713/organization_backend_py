from flask import request

from ..queries import insert_comment


def resolve_get_comments():
    return [
        {"comment": "Comment", "date": "2022/08/08 14:00:00", "author": "Artem"},
        {"comment": "Comment", "date": "2022/08/08 14:00:00", "author": "Artem"},
        {"comment": "Comment", "date": "2022/08/08 14:00:00", "author": "Artem"},
        {"comment": "Comment", "date": "2022/08/08 14:00:00", "author": "Artem"},
        {"comment": "Comment", "date": "2022/08/08 14:00:00", "author": "Artem"},
    ]


def resolve_post_comment():
    attributes = {
        "comment": request.json.get("comment"),
        "user_id": request.json.get("user_id"),
        "event_id": request.json.get("event_id"),
    }

    new_comment = insert_comment(attributes)
    return {
        "comment": new_comment.comment,
    }
