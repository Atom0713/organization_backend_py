from .database import db


def commit_to_db(record: db.Model, multiple: bool = False) -> None:
    db.session.add(record) if not multiple else db.session.add_all(record)
    db.session.commit()
