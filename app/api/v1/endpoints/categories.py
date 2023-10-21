from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Category)
def create_category(
    *,
    db: Session = Depends(get_db),
    category_in: schemas.CategoryCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Optional[models.Category]:
    """Create a new category by superuser."""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You are not a superuser",
        )
    category_name = crud.category.get_by_name(db=db, name=category_in.name)
    if category_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category with name='{category_in.name}' already exists",
        )
    category_slug = crud.category.get_by_slug(db=db, slug=category_in.slug)
    if category_slug:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category with slug='{category_in.slug}' already exists",
        )
    new_category = crud.category.create(db=db, obj_in=category_in)
    return new_category
