import pytest

from fastapi.testclient import TestClient

from src.rest.app import create_app

@pytest.fixture()
def client():
    app = create_app()
    client = TestClient(app)   

    return client
