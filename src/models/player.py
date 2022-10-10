from src.datastore import db

class Player(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    position = db.Column(db.String(20), nullable=False)
    class_rank_id = db.Column(db.Integer, db.ForeignKey("class_rank.id"), nullable=False)
