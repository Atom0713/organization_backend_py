from .queries import get_all_roles, get_user_role_by_id


def resolve_get_user_permissions(user_id: int):
    return get_user_role_by_id(user_id).to_dict()


def resolve_get_all_user_roles():
    roles = get_all_roles()
    return [i.to_dict() for i in roles]
