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

bp = Blueprint("employee-report", __name__, url_prefix="/employee-report")


@bp.route("/", methods=("GET", "POST"))
def report():
    return render_template('employee-report.html')
