import os

import click
import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# =============================
# Application Factory function
# =============================


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)

    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", default="dev"),
        SQLALCHEMY_DATABASE_URI=os.getenv(
            "DATABASE_URI",
            default=f"sqlite:///{os.path.join(app.instance_path, 'flaskr.db')}",
        ),
    )
    # config_type = os.getenv("CONFIG_TYPE", default="config.TestingConfig")
    # app.config.from_object(config_type)

    initialize_extensions(app)
    register_blueprints(app)
    register_cli_commands(app)

    # Check if the database needs initialization
    engine = sqlalchemy.create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    inspector = sqlalchemy.inspect(engine)

    if not inspector.has_table("user"):
        with app.app_context():
            db.drop_all()
            db.create_all()

    return app


# =================
# Helper functions
# =================


def initialize_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    from flaskr import auth, blog

    app.register_blueprint(auth.bp)

    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")


def register_cli_commands(app):
    @app.cli.command("init-db")
    def init_database():
        db.drop_all()
        db.create_all()

        click.echo("Initialized the database.")
