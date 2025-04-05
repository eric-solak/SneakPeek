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

# Dummy blackboard controller
class DummyBlackboardController:
    def __init__(self, image_path, post_details):
        self.image_path = image_path
        self.post_details = post_details

    def identify(self):
        pass

    def getresponse(self):
        return "dummy_result"

def test_identify(client, monkeypatch):
    
    monkeypatch.setattr("app.BlackboardController", DummyBlackboardController)
    
    # Simulate a POST request to /identify
    data = {
        "post_details": "This is the post detaills",
        "post_title": "This is the post title",
        "image": (io.BytesIO(b"testing image"), "test.png")
    }
    response = client.post("/identify", data=data, content_type="multipart/form-data")
    
    # Testing response
    assert response.status_code == 200
    json_data = response.get_json()
    assert "message" in json_data
    assert json_data["message"] == "dummy_result"

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
