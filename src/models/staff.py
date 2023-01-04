from src.datastore import db


class Staff(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    position_id = db.Column(db.Integer, db.ForeignKey("position.id"), nullable=False)

    user = db.relationship("User", back_populates="staff")
    position = db.relationship("Position", back_populates="staff", uselist=False)

    def to_dict(self):
        return self.position.to_dict()