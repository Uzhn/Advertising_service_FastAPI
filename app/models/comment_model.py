from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from app.db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user_model import User
    from .advertisement_model import Advertisement


class Comment(Base):
    description: Mapped[str] = mapped_column(sa.TEXT)
    author_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"), nullable=False)
    ad_id: Mapped[int] = mapped_column(sa.ForeignKey("advertisement.id"), nullable=False)
    pub_date: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True),
        server_default=sa.func.now()
    )

    ad: Mapped["Advertisement"] = relationship(back_populates="comments")
    author: Mapped["User"] = relationship(back_populates="comments")
