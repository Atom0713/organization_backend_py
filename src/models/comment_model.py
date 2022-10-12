from datetime import datetime

from src.datastore import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), nullable=True)
    public = db.Column(db.Boolean, nullable=True, default=0)
    approved = db.Column(db.Boolean, nullable=True, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    user = db.relationship("User", back_populates="comments", uselist=False)

    def to_dict(self):
        return {
            "comment": self.comment,
            "author": self.user.to_dict()["name"],
            "approved": self.approved,
            "public": self.public,
            "date": self.created_at,
        }
