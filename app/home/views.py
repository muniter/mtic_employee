# app/home/views.py

from os import name
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, current_user
from flask_wtf import form

from app.auth.forms import LoginForm

from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return redirect(url_for('auth.login'))


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    #if not current_user.is_admin:
        #abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")

@home.route('/superadmin/dashboard')
@login_required
def superadmin_dashboard():
    # prevent non-admins from accessing the page
    #if not current_user.is_admin:
        #abort(403)

    return render_template('home/superadmin_dashboard.html', title="Dashboard")



