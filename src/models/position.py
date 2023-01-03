from typing import Dict

from src.datastore import db


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)

    def to_dict(self) -> Dict:
        return {"id": self.id, "name": self.name}
