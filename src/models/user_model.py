from src.datastore import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    attendance = db.relationship('Attendance', backref='attendance', lazy=True)
