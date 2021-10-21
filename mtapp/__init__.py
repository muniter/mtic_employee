import os

from flask import Flask, render_template
from mtapp.db import db_session



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'mtapp.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from mtapp import db
    db.init_db()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @app.route("/")
    def index():
        return render_template('index.html')

    from mtapp import employee, user, employee_report
    app.register_blueprint(user.bp)
    app.register_blueprint(employee.bp)
    app.register_blueprint(employee_report.bp)

    return app
