# app/home/views.py

from flask import render_template
from flask_login import login_required

from app.auth.forms import LoginForm

from . import home


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")