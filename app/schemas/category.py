from typing import Optional

from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None


class CategoryCreate(CategoryBase):
    name: str
    slug: str


class CategoryUpdate(CategoryCreate):
    pass


class CategoryInDBBase(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class Category(CategoryInDBBase):
    pass
