from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .advertisement_model import Advertisement  # noqa: F401


class Category(Base):
    name: Mapped[str] = mapped_column(sa.String(length=150), nullable=False, unique=True)
    slug: Mapped[str] = mapped_column(sa.String(length=150), nullable=False, unique=True)

    ads = relationship("Advertisement", back_populates="category")
