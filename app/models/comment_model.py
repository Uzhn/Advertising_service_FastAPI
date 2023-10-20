from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .advertisement_model import Advertisement  # noqa: F401
    from .user_model import User  # noqa: F401


class Comment(Base):
    """Model Comment."""
    description: Mapped[str] = mapped_column(sa.Text)
    author_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"), nullable=False)
    ad_id: Mapped[int] = mapped_column(
        sa.ForeignKey("advertisement.id"), nullable=False
    )
    pub_date: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True), server_default=sa.func.now()
    )

    ad: Mapped["Advertisement"] = relationship(back_populates="comments")
    author: Mapped["User"] = relationship(back_populates="comments")

    def __str__(self):
        return f"Comment(id={self.id!r}, )"

    def __repr__(self) -> str:
        return str(self)
