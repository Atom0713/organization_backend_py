from typing import Dict

from src.datastore import db
from src.models import User


def add_user(attributes: Dict) -> None:
    user = User(**attributes)
    db.session.add(user)
    db.session.commit()
