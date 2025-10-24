import pytest

from app.domain.repository import hero_repo


@pytest.mark.usefixtures("app_ctx")
def test_user_model():
    users = hero_repo.get_all_hero()
    for user in users:
        print(user.name)
