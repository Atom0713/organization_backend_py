from typing import Dict

from src.datastore import commit_to_db
from src.models import Comment


def insert_comment(attributes: Dict) -> "Comment":
    new_comment = Comment(**attributes)
    commit_to_db(new_comment)

    return new_comment
