from typing import Generator, Any

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client() -> Generator[TestClient, Any, None]:
    from app.main import app

    with TestClient(app) as test_client:
        yield test_client
