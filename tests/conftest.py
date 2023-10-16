import os
import tempfile

import pytest

from flaskr import create_app, db
from flaskr.models import Post, User


@pytest.fixture(scope="module")
def test_client():
    os.environ["CONFIG_TYPE"] = "config.TestingConfig"
    app = create_app()

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture(scope="module")
def init_database(test_client):
    db.create_all()

    user1 = User("michaelr", "password")
    user2 = User("other", "password")

    db.session.add_all([user1, user2])
    db.session.commit()

    post1 = Post("first post", "this is a test", user1.id)
    post2 = Post("second post", "this is another test", user2.id)

    db.session.add_all([post1, post2])
    db.session.commit()

    yield

    db.close_all_sessions()
    db.drop_all()


@pytest.fixture(scope="function")
def log_in_default_user(test_client):
    test_client.post(
        "/auth/login", data={"username": "michaelr", "password": "password"}
    )

    yield

    test_client.get("/auth/logout")


@pytest.fixture(scope="module")
def cli_test_client():
    os.environ["CONFIG_TYPE"] = "config.TestingConfig"
    app = create_app()

    runner = app.test_cli_runner()

    yield runner
