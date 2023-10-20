from enum import Enum
from typing import TYPE_CHECKING, List

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .advertisement_model import Advertisement  # noqa: F401
    from .comment_model import Comment  # noqa: F401


class Role(str, Enum):
    """Role of user."""
    USER_ROLE = "USER_ROLE"
    ADMIN_ROLE = "ADMIN_ROLE"
    SUPER_USER_ROLE = "SUPER_USER_ROLE"


class User(Base):
    """Model User."""
    username: Mapped[str] = mapped_column(
        sa.String(length=150), nullable=False, unique=True
    )
    hashed_password: Mapped[str] = mapped_column(sa.String(length=150), nullable=False)
    roles: Mapped[List[Role]] = mapped_column(ARRAY(sa.String))
    is_active: Mapped[bool] = mapped_column(sa.Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(sa.Boolean, default=False)

    ads: Mapped[List["Advertisement"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    comments: Mapped[List["Comment"]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
    )

    @property
    def is_admin(self) -> bool:
        return Role.ADMIN_ROLE in self.roles

    def enrich_admin_roles_by_admin_role(self):
        if not self.is_admin:
            return {*self.roles, Role.ADMIN_ROLE}

    def __str__(self):
        return f"User(id={self.id!r}, username={self.username!r})"

    def __repr__(self) -> str:
        return str(self)
