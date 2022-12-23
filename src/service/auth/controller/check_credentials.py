from typing import Optional

from flask import request

from ..queries import get_user_by_username_password


def check_credentials() -> Optional[int]:
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = get_user_by_username_password(username, password)

    if not user:
        return None
    if len(user) > 1:
        pass  # TODO abort

    return user[0].id
