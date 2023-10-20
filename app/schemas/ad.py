from typing import Optional

from pydantic import BaseModel, ConfigDict


class AdBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None


class AdCreate(AdBase):
    title: str
    description: str
    category_id: int


class AdUpdate(AdBase):
    title: str
    description: str
    category_id: int


class AdInDBBase(AdBase):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class Ad(AdInDBBase):
    pass
