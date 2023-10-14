import pytest
from flask import g, session

from flaskr.models import User

# from flaskr.db import get_db


def test_login_page(test_client):
    response = test_client.get("/auth/login")

    assert response.status_code == 200


def test_valid_login(test_client, init_database):
    response = test_client.post(
        "/auth/login",
        data=dict(username="michaelr", password="password"),
        follow_redirects=True,
    )

    assert response.status_code == 200

    assert b"michaelr" in response.data
    assert b"Log In" not in response.data
    assert b"Log Out" in response.data
    assert b"New" in response.data

    assert g.user.username == "michaelr"

    response = test_client.get("/auth/logout", follow_redirects=True)

    assert response.status_code == 200

    assert b"michaelr" not in response.data
    assert b"Log In" in response.data
    assert b"Log Out" not in response.data
    assert b"Register" in response.data

    assert g.user is None


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("a", "test", b"Incorrect username."),
        ("michaelr", "a", b"Incorrect password."),
    ),
)
def test_invalid_login(test_client, init_database, username, password, message):
    response = test_client.post(
        "/auth/login",
        data=dict(username=username, password=password),
        follow_redirects=True,
    )
    assert response.status_code == 200

    assert message in response.data
    assert b"Logout" not in response.data
    assert b"Log In" in response.data

    assert g.user is None


def test_register(test_client, init_database):
    assert test_client.get("/auth/register").status_code == 200
    response = test_client.post(
        "/auth/register", data={"username": "a", "password": "a"}
    )
    assert response.headers["Location"] == "/auth/login"

    assert User.query.filter_by(username="a").first() is not None


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("", "", b"Username is required."),
        ("a", "", b"Password is required."),
        ("michaelr", "test", b"already registered"),
    ),
)
def test_register_validate_input(
    test_client, init_database, username, password, message
):
    response = test_client.post(
        "/auth/register", data={"username": username, "password": password}
    )
    assert message in response.data
