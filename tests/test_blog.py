import pytest

from flaskr.models import Post


def test_index(test_client, init_database):
    response = test_client.get("/")

    assert b"Flaskr" in response.data
    assert b"Log In" in response.data
    assert b"Register" in response.data


@pytest.mark.parametrize(
    "path",
    (
        "/create",
        "/1/update",
        "/1/delete",
    ),
)
def test_login_required(test_client, init_database, path):
    response = test_client.post(path)
    assert response.headers["Location"] == "/auth/login"


def test_author_required(test_client, init_database, log_in_default_user):
    # Current user can't modify other user's post
    assert test_client.post("/2/update").status_code == 403
    assert test_client.post("/2/delete").status_code == 403

    assert b'href="/2/update"' not in test_client.get("/").data


@pytest.mark.parametrize(
    "path",
    (
        "/3/update",
        "/3/delete",
    ),
)
def test_exists_required(test_client, init_database, log_in_default_user, path):
    assert test_client.post(path).status_code == 404


def test_create(test_client, init_database, log_in_default_user):
    assert test_client.get("/create").status_code == 200
    test_client.post("/create", data={"title": "created", "body": ""})

    posts = Post.query.all()
    assert len(posts) == 3


def test_update(test_client, init_database, log_in_default_user):
    assert test_client.get("/1/update").status_code == 200
    test_client.post("/1/update", data={"title": "updated", "body": ""})

    post = Post.query.filter_by(id=1).first()
    assert post.title == "updated"


@pytest.mark.parametrize(
    "path",
    (
        "/create",
        "/1/update",
    ),
)
def test_create_update_validate(test_client, init_database, log_in_default_user, path):
    response = test_client.post(path, data={"title": "", "body": ""})
    assert b"Title is required." in response.data


def test_delete(test_client, init_database, log_in_default_user):
    response = test_client.post("/1/delete")
    assert response.headers["Location"] == "/"

    post = Post.query.filter_by(id=1).first()
    assert post is None
