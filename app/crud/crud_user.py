from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user_model import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import Hasher


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        new_user = User(
            username=obj_in.username,
            hashed_password=Hasher.get_password_hash(obj_in.hashed_password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def authenticate(self, db: Session, username: str, password: str) -> Optional[User]:
        user = self.get_by_username(db, username=username)
        if not user:
            return None
        if not Hasher.verify_password(password, user.hashed_password):
            return None
        return user


user = CRUDUser(User)
