from typing import Dict

from src.datastore import db


class Attendance(db.Model):
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    present = db.Column(db.Boolean, nullable=False)
    absence_reason = db.Column(db.Text, nullable=True)

    user = db.relationship("User", back_populates="attendance")
    event = db.relationship("Event", back_populates="attendance")

    @classmethod
    def get(cls, event_id: int, user_id: int) -> "Attendance":
        return cls.query.get(event_id, user_id)

    def to_dict(self) -> Dict:
        user = self.user.to_dict()
        return {
            "present": self.present,
            "absence_reason": self.absence_reason,
            "first_name": user['first_name'],
            "last_name": user['last_name'],
            "user_id": user['id'],
        }
