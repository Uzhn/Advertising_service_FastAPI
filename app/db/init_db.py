from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401
from app.core.security import Hasher
from app.models.user_model import Role


def init_db(db: Session) -> None:

    user = crud.user.get_by_username(db, username=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            username=settings.FIRST_SUPERUSER,
            hashed_password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            roles=[Role.SUPER_USER_ROLE]
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
