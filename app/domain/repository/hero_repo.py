from typing import Sequence

from sqlalchemy import select

from app.domain.models import Hero, db


def get_all_hero() -> Sequence[Hero]:
    statement = select(Hero)
    return db.session.scalars(statement).all()
