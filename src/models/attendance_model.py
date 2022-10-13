from typing import Dict

from src.datastore import db


class Attendance(db.Model):
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    present = db.Column(db.Boolean, nullable=False)
    absence_reason = db.Column(db.Text, nullable=True)

    user = db.relationship("User", back_populates="attendance")
    event = db.relationship("Event", back_populates="attendance")

    def to_dict(self) -> Dict:
        return {
            "present": self.present,
            "absence_reason": self.absence_reason,
            "user": self.user.to_dict(),
        }
