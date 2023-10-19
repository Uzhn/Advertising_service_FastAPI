from typing import TYPE_CHECKING, List

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .advertisement_model import Advertisement  # noqa: F401


class User(Base):
    username: Mapped[str] = mapped_column(sa.String(length=150), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(sa.String(length=150), nullable=False)

    ads: Mapped[List["Advertisement"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )

    def __str__(self):
        return f"User(id={self.id!r}, username={self.username!r})"

    def __repr__(self) -> str:
        return str(self)
