from src.datastore import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # Auto increment?
    name = db.Column(db.String(20), nullable=False)
    user = db.relationship('User', backref='user', lazy=True)
