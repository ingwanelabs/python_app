import pytest
from hello import app  # Adjust this import to your actual app module

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get("/")
    assert response.data == b"<p>Hello, World!</p>"
    assert response.status_code == 200
