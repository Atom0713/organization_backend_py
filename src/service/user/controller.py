from datetime import datetime
from typing import Dict, List
from uuid import uuid4

from flask import abort, request
from flask_jwt_extended import get_jwt_identity

from src.service.queries import (get_all_users_by_role_id, get_role_name_by_id,
                                 insert_user, query_user_by_id)

from ..utils import DATE_FORMAT, ROLES, logger


def resolve_get_user() -> Dict:
    user_id: int = get_jwt_identity()
    return query_user_by_id(user_id).to_dict()


def resolve_get_user_by_id(user_id: int) -> Dict:
    return query_user_by_id(user_id).to_dict()


def resolve_get_users_by_role(role_id: int) -> List[dict]:
    return {"data": [user.to_dict() for user in get_all_users_by_role_id(role_id)]}


def resolve_add_user() -> Dict:
    new_user_role_id = request.json.get("role_id")
    new_user_role_name = get_role_name_by_id(new_user_role_id)

    requester_user = query_user_by_id(get_jwt_identity())

    if (
        new_user_role_name == ROLES.ADMIN
        and not requester_user.role.name == ROLES.ADMIN
    ):
        logger.error(
            f"User with role: {requester_user.role.name} trying to create ADMIN user. user_id: {requester_user.id}"
        )
        abort(401, "Not allowed. Non Admin can't create Admin user.")

    email = request.json.get("email")
    password = uuid4().hex[0:10]
    attributes = {
        "email": email,
        "first_name": request.json.get("first_name"),
        "last_name": request.json.get("last_name"),
        "dob": datetime.strptime(request.json.get("dob"), DATE_FORMAT),
        "role_id": new_user_role_id,
        "password": password,
    }

    if new_user_role_name == ROLES.STAFF:
        attributes["staff_details"] = {
            "position": request.json.get("position"),
        }
    elif new_user_role_name == ROLES.PLAYER:
        attributes["player_details"] = {
            "position": request.json.get("position"),
            "height": request.json.get("height"),
            "weight": request.json.get("weight"),
        }

    new_user = insert_user(attributes)
    # TODO send email?

    return new_user.to_dict()
