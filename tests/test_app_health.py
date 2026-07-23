from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

REQUIRED_ENDPOINTS = [
    "/",
    "/health",
    "/api/health",
    "/api/alpha/gaurangga/sync-status",
]


@pytest.mark.parametrize("path", REQUIRED_ENDPOINTS)
def test_endpoint_available(path):
    response = client.get(path)
    assert response.status_code == 200, f"GET {path} returned {response.status_code}"


def test_health_response_shape():
    response = client.get("/health")
    body = response.json()
    assert body["status"] == "healthy"
    assert "service" in body
    assert "version" in body


def test_api_health_response_shape():
    response = client.get("/api/health")
    body = response.json()
    assert body["status"] == "ok"
    assert "api_version" in body


def test_sync_status_always_returns_200_even_without_data_files():
    response = client.get("/api/alpha/gaurangga/sync-status")
    assert response.status_code == 200
    body = response.json()
    assert "status" in body
    assert "timestamp" in body


def test_consolidated_status_returns_200_or_500_without_data():
    response = client.get("/api/alpha/gaurangga/consolidated-status")
    assert response.status_code in (200, 500)


def test_nodes_status_returns_200_or_500_without_data():
    response = client.get("/api/alpha/gaurangga/nodes")
    assert response.status_code in (200, 500)
