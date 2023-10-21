from typing import Optional

from fastapi.encoders import jsonable_encoder

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def get_by_name(self, db: Session, name: str) -> Optional[Category]:
        """Get category by name."""
        get_category = select(Category).filter(Category.name == name)
        return db.scalar(get_category)

    def get_by_slug(self, db: Session, slug: str) -> Optional[Category]:
        """Get category by slug."""
        get_category = select(Category).filter(Category.slug == slug)
        return db.scalar(get_category)


category = CRUDCategory(Category)
