from typing import Dict, List

from src.datastore import commit_to_db
from src.models import Comment


def insert_comment(attributes: Dict) -> "Comment":
    new_comment = Comment(**attributes)
    commit_to_db(new_comment)

    return new_comment


def query_event_comments(event_id: int) -> List[Comment]:
    return Comment.query.filter(Comment.event_id == event_id).filter_by(public=False).all()
