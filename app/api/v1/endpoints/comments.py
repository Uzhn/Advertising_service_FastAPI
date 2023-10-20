from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.db.session import get_db

router = APIRouter()


@router.post("/{ad_id}/new_comment", response_model=schemas.Comment)
def create_comment(
    *,
    db: Session = Depends(get_db),
    comment_in: schemas.CommentCreate,
    ad_id: int,
    current_user: models.User = Depends(deps.get_current_user),
) -> Optional[models.Comment]:
    """Create new comment."""
    ad = crud.ad.get(db=db, id=ad_id)
    if not ad:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Advertisement with id={ad_id} not found",
        )
    new_comment = crud.comment.create_new_comment(
        db=db,
        obj_in=comment_in,
        author_id=current_user.id,
        ad_id=ad.id,
    )
    return new_comment


@router.delete("/{ad_id}/comment/{comment_id}", response_model=schemas.Comment)
def delete_comment(
    *,
    db: Session = Depends(get_db),
    ad_id: int,
    comment_id: int,
    current_user: models.User = Depends(deps.get_current_user),
) -> Optional[models.Comment]:
    """Delete comment."""
    ad = crud.ad.get(db=db, id=ad_id)
    if not ad:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Advertisement with id={ad_id} not found",
        )
    comment = crud.comment.get(db=db, id=comment_id)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Comment with id={ad_id} not found",
        )
    if not (current_user.is_superuser or current_user.is_admin) and (
        comment.author_id != current_user.id
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough permissions"
        )
    comment = crud.comment.remove(db=db, id=comment_id)
    return comment
