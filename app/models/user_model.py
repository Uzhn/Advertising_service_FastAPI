import sqlalchemy as sa
from sqlalchemy.orm import mapped_column, Mapped

from app.db.base_class import Base


class User(Base):
    username: Mapped[str] = mapped_column(sa.String(length=150), nullable=False)
    password: Mapped[str] = mapped_column(sa.String(length=150), nullable=False)