from src.datastore import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), nullable=True)
    public = db.Column(db.Boolean, nullable=True)
    approved = db.Column(db.Boolean, nullable=True)

    def to_dict(self):  # for build json format
        return {
            "comment": self.comment,
            "approved": self.approved,
            "public": self.public,
        }