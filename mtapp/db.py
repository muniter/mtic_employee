import click
from flask import g
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from mtapp import app

engine = None
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db(app=None):
    """Initialize the databse, deleting previous data."""
    import mtapp.models
    Base.metadata.create_all(bind=engine)
    # TODO: Initialization of some records (superuser and group)

def init_engine(app):
    """Start the database engine."""
    global engine
    engine = create_engine(app.config['DATABASE'])
    Base.metadata.create_all(bind=engine)

@click.command("initdb")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

def close_session(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db_session.remove()


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_session)
    app.cli.add_command(init_db_command).close()
