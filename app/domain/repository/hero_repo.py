from typing import Sequence

from sqlalchemy import select

from app.domain.models import Hero, db


def get_all_hero() -> Sequence[Hero]:
    return Hero.query.all()
