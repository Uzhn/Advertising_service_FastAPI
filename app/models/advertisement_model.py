from typing import TYPE_CHECKING, List

import sqlalchemy as sa
from app.db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from .category_model import Category  # noqa: F401
    from .user_model import User  # noqa: F401
    from .comment_model import Comment  # noqa: F401


class Advertisement(Base):
    title: Mapped[str] = mapped_column(sa.String(length=120), nullable=False)
    description: Mapped[str] = mapped_column(sa.Text, nullable=False)
    category_id: Mapped[int] = mapped_column(sa.ForeignKey("category.id"), nullable=False)
    owner_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"), nullable=False)

    category: Mapped["Category"] = relationship(back_populates="ads")
    owner: Mapped["User"] = relationship(back_populates="ads")
    comments: Mapped[List["Comment"]] = relationship(
        back_populates="ad",
        cascade="all, delete-orphan",
    )

    def __str__(self):
        return f"Advertisement(title={self.title!r})"

    def __repr__(self) -> str:
        return str(self)
