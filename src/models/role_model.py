from src.datastore import db


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto increment?
    name = db.Column(db.String(20), nullable=False)
    user = db.relationship("User", backref="role", lazy=True)

    @classmethod
    def get(cls, role_id: int) -> "Role":
        return cls.query.get(role_id)

    def to_dict(self):  # for build json format
        return {"id": self.id, "name": self.name}
