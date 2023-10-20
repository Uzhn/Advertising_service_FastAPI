from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.db.session import get_db
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Ad])
def get_all_ads(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    ads = crud.ad.get_multi(db=db, skip=skip, limit=limit)
    return ads


@router.get("/{ad_id}", response_model=schemas.Ad)
def get_ad(
    ad_id: int,
    db: Session = Depends(get_db),
):
    ad = crud.ad.get(db=db, id=ad_id)
    if not ad:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ad with id={ad_id} not found",
        )
    return ad


@router.post("/create_ad", response_model=schemas.Ad)
def create_ad(
    *,
    db: Session = Depends(get_db),
    ad_in: schemas.AdCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    ad = crud.ad.create_with_owner(db=db, obj_in=ad_in, owner_id=current_user.id)
    return ad


@router.delete("/delete_ad/{ad_id}", response_model=schemas.Ad)
def delete_ad(
    *,
    ad_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    ad = crud.ad.get(db=db, id=ad_id)
    if not ad:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ad with id={ad_id} not found",
        )
    if ad.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough permissions"
        )
    ad = crud.ad.remove(db=db, id=ad_id)
    return ad
