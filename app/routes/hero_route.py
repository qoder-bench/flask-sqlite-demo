from flask import Blueprint, jsonify

from app.domain.repository import hero_repo

hero_router = Blueprint("heros", __name__, template_folder="templates")


@hero_router.route("")
def hero_list():
    users = hero_repo.get_all_hero()
    return jsonify([{"id": user.id, "name": user.name} for user in users])
