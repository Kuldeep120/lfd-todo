from fastapi.testclient import TestClient 
from starlette.testclient import TestClient
from unittest import TestCase

from main import app
record_id = 0
client = TestClient(app)
import pytest

@pytest.fixture
def data():
    pytest.record_id = 0

def test_create_todo():
    response = client.post(
        "/todo/",
        json={"title": "Todo 1", "description": "Todo Description 1"},
    )

    assert response.status_code == 201
    resp = response.json()
    try:
        pytest.record_id = resp['id']
        del resp['id']

    except:
        pass
    assert resp == {"title": "Todo 1",
     "description": "Todo Description 1"}


def test_get_todo():
    response = client.get(
        "/todo/%s"%pytest.record_id
    )
    import pdb
    pdb.set_trace()
    assert response.status_code == 200
    # response.json() == 

def test_update_todo():
    response = client.put(
        "/todo/%s"%pytest.record_id,
        json = {"title": "Todo Updated 1",
     "description": "Todo Description 1"}
    )

    assert response.status_code == 202

def test_get_all_todo():
    response = client.get(
        "/todo/?skip=0&limit=100",
        json = {"title": "Todo Updated 1",
     "description": "Todo Description 1"}
    )
    assert response.status_code == 200

def test_delete_todo():
    response = client.delete(
        '/todo/%s'%pytest.record_id
        )

    assert response.status_code == 204
