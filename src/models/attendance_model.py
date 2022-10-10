from src.datastore import db

class Attendance(db.Model):
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    present = db.Column(db.Boolean, nullable=False)
    absence_reason = db.Column(db.Text, nullable=True)