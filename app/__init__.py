# third-party imports
from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import sqlite3

# local imports
from settings import app_config


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['SECRET_KEY'] = 'the random string'
    #app.config.from_object(app_config[config_name])
    #app.config.from_pyfile('config.py')

    from app import models
    
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/employee.db'    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True    
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    # from .admin import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('home/404.html', title='Page Not Found'), 404

    return app
