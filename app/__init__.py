import logging
import click

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from sqlalchemy import event
from sqlalchemy.engine import Engine

from .security import MySecurityManager

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)


app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, security_manager_class=MySecurityManager)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

@app.cli.command("initdata")
def init_db():
    from .test_data import deps


from . import models, views  # noqa
