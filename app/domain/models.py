from typing import Optional

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Integer, Text, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class BaseDictModel(db.Model):
    __abstract__ = True

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Hero(BaseDictModel):
    __tablename__ = "hero"

    name: Mapped[str] = mapped_column(Text)
    power: Mapped[str] = mapped_column(Text)
    age: Mapped[int] = mapped_column(Integer)
    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("current_timestamp")
    )
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("current_timestamp")
    )
