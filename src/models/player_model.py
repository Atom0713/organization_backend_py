from src.datastore import db


class Player(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    position = db.Column(db.String(20), nullable=False)
    user = db.relationship("User", back_populates="player")

    def to_dict(self):  # for build json format
        return {
            "height": self.height,
            "weight": self.weight,
            "position": self.position,
        }
