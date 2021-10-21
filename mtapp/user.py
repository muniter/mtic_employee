from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from mtapp.auth import login_required
# from mtapp.db import get_db

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/", methods=['GET'])
def user():
    print("Hitting user")
    data = {"title": "Usuario"}
    return render_template('user.html')
