from typing import Dict
from src.models import User
from src.datastore import db


def add_user(attributes: Dict) -> None:
    user = User(**attributes)
    db.session.add(user)
    db.session.commit()
