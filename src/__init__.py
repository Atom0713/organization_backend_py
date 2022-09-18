import os

from flask import Flask
from flask_cors import CORS


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )
    CORS(app, resource={r"/*": {"origins": "*"}})
    # CORS(app, origins=os.environ.get("CLIENT_URL", ["http://localhost:3000", "https://antalya-vandals-dashboard.herokuapp.com/"]))

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

    from .service.attendance import attendance
    from .service.auth import bp as auth
    from .service.comment import COMMENT
    from .service.common import bp as common
    from .service.events import EVENTS
    from .service.roles import ROLE
    from .service.user import bp as user

    app.register_blueprint(common)
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(ROLE)
    app.register_blueprint(EVENTS)
    app.register_blueprint(attendance)
    app.register_blueprint(COMMENT)

    return app
