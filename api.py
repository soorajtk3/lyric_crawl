from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.route("/artist")
def get_artists():
    return jsonify({"name": "sooraj"})
