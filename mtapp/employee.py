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

bp = Blueprint("employee", __name__, url_prefix="/employee")

@bp.route("/", methods=("GET", "POST"))
def index():
    return render_template('employee.html')

