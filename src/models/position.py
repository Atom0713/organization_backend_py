from typing import Dict, List

from src.datastore import db


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)

    player = db.relationship("Player", back_populates="position")
    staff = db.relationship("Staff", back_populates="position")

    @classmethod
    def get_all(cls) -> List["Position"]:
        return Position.query.all()

    def to_dict(self) -> Dict:
        return {"id": self.id, "name": self.name}
