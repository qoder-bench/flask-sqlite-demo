from flask import Blueprint

from app.domain.repository import hero_repo

hero_router = Blueprint("heros", __name__, template_folder="templates")


@hero_router.route("")
def hero_list():
    users = hero_repo.get_all_hero()
    return [user.to_dict() for user in users]
