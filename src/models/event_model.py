from src.datastore import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    attendance = db.relationship("Attendance", backref="attendance", lazy=True)
