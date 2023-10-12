import os
import sqlite3

import click
import pymysql
from dotenv import load_dotenv
from flask import current_app, g

load_dotenv()

db_host = os.environ["DB_HOST"]
db_user = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]


def get_db():
    if "db" not in g:
        g.db = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor,
        )

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


# def init_db():
#     db = get_db()

#     with current_app.open_resource("schema.sql") as f:
#         db.executescript(f.read().decode("utf8"))


# @click.command("init-db")
# def init_db_command():
#     """Clear the existing data and create new tables."""
#     init_db()
#     click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    # app.cli.add_command(init_db_command)
