import imp
from flask import request, jsonify, Blueprint
from flask_cors import CORS, cross_origin


bp = Blueprint('user', __name__, url_prefix="/user")

cors = CORS(bp, resources={r"/foo": {"origins": "http://localhost:3000"}})

@bp.route("/", methods=["GET"])
@cross_origin(origin='localhost', headers=['Authorization'])
def get_user():
    print(request.headers)

    return jsonify({"name": "Artem Sliusarenko"})
