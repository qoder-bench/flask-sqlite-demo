import pytest

from app.domain.models import Hero
from app.domain.repository import hero_repo


@pytest.mark.usefixtures("app_ctx")
def test_user_model():
    users = Hero.query.all()
    for user in users:
        print(user.to_dict())
