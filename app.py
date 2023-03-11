from src import create_app
from src.datastore import db

app = create_app()
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
