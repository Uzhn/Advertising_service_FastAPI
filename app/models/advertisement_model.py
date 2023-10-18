from typing import TYPE_CHECKING

import sqlalchemy as sa
from app.db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .user_model import User

if TYPE_CHECKING:
    from .category_model import Category  # noqa: F401


class Advertisement(Base):
    title: Mapped[str] = mapped_column(sa.String(length=120), nullable=False)
    description: Mapped[str] = mapped_column(sa.String(length=500), nullable=False)
    category_id: Mapped[int] = mapped_column(sa.ForeignKey("category.id"), nullable=False)
    owner_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"), nullable=False)

    category = relationship("Category", back_populates="ads")
    owner = relationship("User", back_populates="ads")
