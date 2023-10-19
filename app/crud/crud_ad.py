from typing import Any, Dict, Optional, Union, List, Type

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase, ModelType
from app.models import Advertisement
from app.schemas.ad import AdCreate, AdUpdate, Ad


class CRUDAd(CRUDBase[Advertisement, AdCreate, AdUpdate]):
    def create_with_owner(
            self, db: Session, *, obj_in: AdCreate, owner_id: int
    ) -> Advertisement:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj




ad = CRUDAd(Advertisement)
