import pytest
from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client
