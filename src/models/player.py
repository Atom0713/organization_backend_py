from src.datastore import db


class Player(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    position_id = db.Column(db.Integer, db.ForeignKey("position.id"), nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    user = db.relationship("User", back_populates="player")
    position = db.relationship("Position", back_populates="player", uselist=False)

    def to_dict(self):  # for build json format
        return {
            "height": self.height,
            "weight": self.weight,
        }
