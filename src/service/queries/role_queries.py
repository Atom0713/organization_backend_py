from src.models import Role


def get_role_name_by_id(role_id: int) -> str:
    return Role.get(role_id).name
