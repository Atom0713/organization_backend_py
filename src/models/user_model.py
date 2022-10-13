from src.datastore import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)

    attendance = db.relationship("Attendance", back_populates="user", lazy=True)
    staff = db.relationship("Staff", back_populates="user", uselist=False)
    player = db.relationship("Player", back_populates="user", uselist=False)
    role = db.relationship("Role", back_populates="user", uselist=False)
    comments = db.relationship("Comment", back_populates="user")

    @classmethod
    def get(cls, user_id: int) -> "User":
        return cls.query.get(user_id)

    def to_dict(self):  # for build json format
        user_details = {
            "id": self.id,
            "name": f"{self.first_name} {self.last_name}",
            "email": self.email,
            "dob": self.dob,
            "role": self.role.to_dict(),
        }
        if self.staff:
            user_details = {**user_details, **self.staff.to_dict()}
        if self.player:
            user_details = {**user_details, **self.player.to_dict()}

        return user_details
