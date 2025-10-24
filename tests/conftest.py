import pytest

from app.main import app


@pytest.fixture()
def test_app():
    yield app


@pytest.fixture
def app_ctx(test_app):
    with test_app.app_context():
        yield
