from typing import Dict, List

from src.datastore import db
from src.models import Player, Staff, User


def query_user_by_id(user_id: int) -> User:
    return User.get(user_id)


def get_all_users_by_role_id(role_id: int) -> List[User]:
    user = (
        User.query.filter(User.role_id == role_id)
        .join(Staff, Staff.user_id == User.id, isouter=True)
        .join(Player, Player.user_id == User.id, isouter=True)
        .all()
    )
    return user


def insert_user(attributes: Dict) -> None:
    staff_details = attributes.pop("staff_details", None)
    player_details = attributes.pop("player_details", None)
    user = User(**attributes)

    if staff_details:
        user.staff = Staff(**staff_details)

    if player_details:
        user.player = Player(**player_details)

    db.session.add(user)
    db.session.commit()
