from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from app.models.user_model import Role


class UserBase(BaseModel):
    username: Optional[str] = None
    hashed_password: Optional[str] = None


class UserCreate(UserBase):
    username: str
    hashed_password: str


class SuperUserCreate(UserCreate):
    is_superuser: bool
    roles: List[Role]


class UserUpdate(UserBase):
    hashed_password: Optional[str] = None
    roles: List[Role]


class UserInDBBase(UserBase):
    id: Optional[int] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    roles: List[Role] = [Role.USER_ROLE]

    model_config = ConfigDict(from_attributes=True)


class User(UserInDBBase):
    pass


class UpdatedUserPrivilege(BaseModel):
    id: int
    username: str
    roles: List[Role]
