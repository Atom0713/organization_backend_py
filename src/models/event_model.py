from typing import Dict, List

from src.datastore import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=0)

    attendance = db.relationship("Attendance", backref="event", lazy=True)
    comments = db.relationship("Comment", backref="event", lazy=True)

    @classmethod
    def get(cls, event_id: int) -> "Event":
        return Event.query.get(event_id)

    @classmethod
    def get_all(cls) -> List["Event"]:
        return Event.query.all()

    def to_dict(self, show_additional=True) -> Dict:
        event_details = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "location": self.location,
            "date": self.date,
            "completed": self.completed,
        }
        if show_additional:
            event_details["attendance"] = self.attendance
            event_details["comments"] = [comment.to_dict() for comment in self.comments]

        return event_details
