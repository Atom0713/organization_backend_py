import datetime
import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        JWT_SECRET_KEY="super-secret",
        JWT_ACCESS_TOKEN_EXPIRES=datetime.timedelta(days=1, seconds=5),
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            "MYSQL_DATABASE_URI"
        ),
    )

    CORS(app, resource={r"/*": {"origins": "*"}})
    JWTManager(app)
    # CORS(app, origins=os.environ.get(
    # "CLIENT_URL", ["http://localhost:3000", "https://antalya-vandals-dashboard.herokuapp.com/"]))

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .service.auth import bp as auth
    from .service.comment import COMMENT
    from .service.common import bp as common
    from .service.events import EVENTS
    from .service.positions import bp as positions
    from .service.roles import ROLE
    from .service.user import bp as user

    app.register_blueprint(common)
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(ROLE)
    app.register_blueprint(EVENTS)
    app.register_blueprint(COMMENT)
    app.register_blueprint(positions)

    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()

    return app
