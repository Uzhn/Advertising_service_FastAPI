from typing import Any

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, as_declarative, declared_attr, mapped_column


@as_declarative()
class Base:
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
