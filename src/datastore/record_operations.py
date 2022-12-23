from .database import db


def commit_to_db(record) -> None:
    db.session.add(record)
    db.session.commit()
