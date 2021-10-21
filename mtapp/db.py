from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/test.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import mtapp.models
    Base.metadata.create_all(bind=engine)

# import sqlite3

# import click
# from flask import current_app
# from flask import g
# from flask.cli import with_appcontext


# def get_db():
#     """Connect to the application's configured database. The connection
#     is unique for each request and will be reused if this is called
#     again.
#     """
#     if "db" not in g:
#         g.db = sqlite3.connect(
#             current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         g.db.row_factory = sqlite3.Row

#     return g.db


# def close_db(e=None):
#     """If this request connected to the database, close the
#     connection.
#     """
#     db = g.pop("db", None)

#     if db is not None:
#         db.close()


# def init_db():
#     """Clear existing data and create new tables."""
#     return
#     # db = get_db()

#     # with current_app.open_resource("schema.sql") as f:
#     #     db.executescript(f.read().decode("utf8"))


# @click.command("init-db")
# @with_appcontext
# def init_db_command():
#     """Clear existing data and create new tables."""
#     init_db()
#     click.echo("Initialized the database.")


# def init_app(app):
#     """Register database functions with the Flask app. This is called by
#     the application factory.
#     """
#     app.teardown_appcontext(close_db)
#     app.cli.add_command(init_db_command).close()