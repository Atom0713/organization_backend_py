from src.datastore import db

class ClassRank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    user = db.relationship('Player', backref='player', lazy=True)