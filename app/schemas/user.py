from typing import Optional, List

from pydantic import BaseModel, ConfigDict

from app.models.user_model import Role


class UserBase(BaseModel):
    username: Optional[str] = None
    hashed_password: Optional[str] = None


class UserCreate(UserBase):
    username: str
    hashed_password: str
    is_active: Optional[bool] = True
    is_superuser: bool = False
    roles: List[Role] = [Role.USER_ROLE]


class UserUpdate(UserBase):
    hashed_password: Optional[str] = None
    roles: List[Role]


class UserInDBBase(UserCreate):
    id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class User(UserInDBBase):
    pass


class UpdatedUserPrivilege(BaseModel):
    id: int
    username: str
    roles: List[Role]
