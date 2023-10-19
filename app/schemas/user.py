from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: Optional[str] = None
    hashed_password: Optional[str] = None


class UserCreate(UserBase):
    username: str
    hashed_password: str


class UserUpdate(UserBase):
    hashed_password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class User(UserInDBBase):
    pass
