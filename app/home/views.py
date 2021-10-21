# app/home/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required
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