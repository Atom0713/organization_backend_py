from typing import List

from src.models import Role, User


def get_user_role_by_id(user_id: int) -> Role:
    user = User.get(user_id)
    return Role.get(user.role_id)


def get_all_roles() -> List[Role]:
    return Role.query.all()
