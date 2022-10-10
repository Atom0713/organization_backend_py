from uuid import uuid4

from flask import request

from ..utils import logger
from .queries import add_user


def resolve_get_users_by_role(role_id):

    users = {
        "2": [
            {
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "birth_date": "05/04/1996",
                "positions": "CB/LB",
            },
            {
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "birth_date": "05/04/1996",
                "positions": "CB/LB",
            },
            {
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "birth_date": "05/04/1996",
                "positions": "CB/LB",
            },
            {
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "birth_date": "05/04/1996",
                "positions": "CB/LB",
            },
        ],
        "3": [
            {
                "id": 1,
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "height": "175",
                "weight": "75",
                "position": "CB",
                "birth_date": "05/04/1996",
            },
            {
                "id": 2,
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "height": "175",
                "weight": "75",
                "position": "CB",
                "birth_date": "05/04/1996",
            },
            {
                "id": 3,
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "height": "175",
                "weight": "75",
                "position": "CB",
                "birth_date": "05/04/1996",
            },
            {
                "id": 4,
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "height": "175",
                "weight": "75",
                "position": "CB",
                "birth_date": "05/04/1996",
            },
            {
                "id": 5,
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "height": "175",
                "weight": "75",
                "position": "CB",
                "birth_date": "05/04/1996",
            },
            {
                "id": 6,
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "height": "175",
                "weight": "75",
                "position": "CB",
                "birth_date": "05/04/1996",
            },
        ],
    }

    return users[role_id]


def resolve_add_user():
    email = request.json.get("email")
    password = uuid4().hex[0:10]
    attributes = {
        "email": email,
        "first_name": request.json.get("first_name"),
        "last_name": request.json.get("last_name"),
        "dob": request.json.get("dob"),
        "role_id": request.json.get("role_id"),
        "password": password,
    }
    add_user(attributes)
    # TODO send email?

    return email
