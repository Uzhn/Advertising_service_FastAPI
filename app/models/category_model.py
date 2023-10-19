from typing import TYPE_CHECKING, List

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .advertisement_model import Advertisement  # noqa: F401


class Category(Base):
    name: Mapped[str] = mapped_column(sa.String(length=150), nullable=False, unique=True)
    slug: Mapped[str] = mapped_column(sa.String(length=150), nullable=False, unique=True)

    ads: Mapped[List["Advertisement"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan",
    )

    def __str__(self):
        return f"Category(name={self.name!r})"

    def __repr__(self) -> str:
        return str(self)
