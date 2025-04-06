import io
import pytest
from app import app
from db_setup import setup_db, add_data_test

# Setup stuff
@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
    with app.app_context():
        setup_db()
    
    with app.test_client() as client:
        yield client

def test_get_posts(client):
    with app.app_context():
        add_data_test()

    # Simulating a GET request to /get-posts
    response = client.get("/get-posts")
    assert response.status_code == 200
    json_data = response.get_json()

    # Making sure the json is structure right
    assert "posts" in json_data
    for post in json_data["posts"]:
        assert "pid" in post
        assert "image_path" in post
        assert "description" in post
        assert "rating" in post

def test_get_comments(client):
    with app.app_context():
        add_data_test()

    response = client.get("/get-comments")
    assert response.status_code == 200
    json_data = response.get_json()

    assert "comments" in json_data
    for comment in json_data["comments"]:
        assert "cid" in comment
        assert "body" in comment

def test_get_identifications(client):
    with app.app_context():
        add_data_test()

    response = client.get("/get-identification?pid=1")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "identification" in json_data
