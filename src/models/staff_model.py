from src.datastore import db


class Staff(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    position = db.Column(db.String(20), nullable=False)
    user = db.relationship("User", back_populates="staff")

    def to_dict(self):  # for build json format
        return {
            "position": self.position,
        }
