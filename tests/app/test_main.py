from fastapi.testclient import TestClient


class TestAPI:
    @staticmethod
    def test_health_returns_healthy(
        client: TestClient,
    ):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}
