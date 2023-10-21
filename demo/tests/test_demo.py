import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient
from starlette import status
from demo.web.application import get_app
from unittest.mock import patch


def test_health_check():
    """
    Checks the health endpoint.
    """
    client = TestClient(get_app())
    response = client.get("/api/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "OK"}

@patch('demo.web.api.monitoring.views.health_check', side_effect=Exception('Server error'))
def test_health_check_server_error(mocked_health_check):
    """
    Checks the health endpoint for server error.
    """
    client = TestClient(get_app())
    response = client.get("/api/health")
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": "API is not healthy"}
