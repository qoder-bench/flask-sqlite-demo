import pytest

from app.domain.models import Hero


@pytest.mark.usefixtures("app_ctx")
def test_user_model():
    users = Hero.query.all()
    for user in users:
        print(user.to_dict())


@pytest.mark.usefixtures("app_ctx")
def test_user_query():
    user = Hero.query.where(Hero.name == "Batman").first()
    print(user.to_dict())
