from src.models import User


def get_user_by_username_password(username: str, password: str):
    return User.query.filter(User.email == username).filter(User.password == password).all()
