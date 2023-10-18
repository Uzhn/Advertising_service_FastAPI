import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class User(Base):
    username: Mapped[str] = mapped_column(sa.String(length=150), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(sa.String(length=150), nullable=False)
