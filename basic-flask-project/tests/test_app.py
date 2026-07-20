from app import app


def test_home_page_returns_success():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Basic Flask Project" in response.data
    assert b"Flask Starter" in response.data


def test_health_endpoint_returns_ok_json():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"status": "ok"}


def test_unknown_route_returns_404():
    client = app.test_client()

    response = client.get("/missing")

    assert response.status_code == 404
