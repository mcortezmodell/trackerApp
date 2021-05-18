import sqlite3

import click 
from flask import current_app, g 
from flask.cli import with_appcontext

# connect to app's configured db 
def get_db():
    # use global object to check if db exists, if not create file
    if "db" not in g: 
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db 

# if the request is connected to the db, close connection
def close_db(e=None):
    db = g.pop("db", None)
    # auto-close to avoid memory leaks 
    if db is not None: 
        db.close()


# clear existing data and create new tables 
def init_db():
    db = get_db
    # read sql schema 
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

# initialize db in command line
@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")

# register database functions with the Flask app
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)