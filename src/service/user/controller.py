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
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "height": "175",
                "weight": "75",
                "position": "CB",
                "birth_date": "05/04/1996",
            },
            {
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "height": "175",
                "weight": "75",
                "position": "CB",
                "birth_date": "05/04/1996",
            },
            {
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "height": "175",
                "weight": "75",
                "position": "CB",
                "birth_date": "05/04/1996",
            },
            {
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "height": "175",
                "weight": "75",
                "position": "CB",
                "birth_date": "05/04/1996",
            },
            {
                "img": "assets/images/faces/face1.jpg",
                "name": "Artem",
                "height": "175",
                "weight": "75",
                "position": "CB",
                "birth_date": "05/04/1996",
            },
            {
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
    return {"password": "iyutrsergh", "username": "hj@mail.com"}


def resolve_get_all_user_roles():
    return {
        "user_roles": [
            {"id": 1, "name": "Admin"},
            {"id": 2, "name": "Staff"},
            {"id": 3, "name": "Player"},
        ]
    }
