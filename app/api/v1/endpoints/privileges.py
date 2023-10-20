from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.db.session import get_db

router = APIRouter()


@router.post("/grant_admin_privilege", response_model=schemas.UpdatedUserPrivilege)
def grant_admin_privilege(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Optional[models.User]:
    """
    Promotes a user to admin status.
    """
    if not (current_user.is_superuser or current_user.is_admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have admin or superuser rights.",
        )
    if current_user.id == user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot manage privileges of itself.",
        )
    user_for_promotion = crud.user.get_by_id(db=db, user_id=user_id)
    if not user_for_promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id={user_id} not found.",
        )
    if user_for_promotion.is_admin or user_for_promotion.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with id={user_id} already promoted to admin.",
        )
    updated_user_params = {
        "roles": user_for_promotion.enrich_admin_roles_by_admin_role()
    }
    updated_user = crud.user.update(
        db=db,
        obj_in=updated_user_params,
        db_obj=user_for_promotion,
    )
    return updated_user
