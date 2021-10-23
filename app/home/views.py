# app/home/views.py

from os import name
from flask import flash, redirect, render_template, url_for, abort
from flask_login import login_required, current_user
from flask_wtf import form

# imports local
from ..models import Employee

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
    if not current_user.role_id == 2:
        abort(403)

    employees = Employee.query.all()
    return render_template('home/admin_dashboard.html', employees=employees, title="Dashboard")

@home.route('/superadmin/dashboard')
@login_required
def superadmin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.role_id == 1:
        abort(403)
    
    employees = Employee.query.all()
    return render_template('home/superadmin_dashboard.html',
                           employees=employees, title='Dashboard')



