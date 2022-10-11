from src.models import User


def query_user_by_id(user_id: int) -> User:
    return User.get(user_id)
