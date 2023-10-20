from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Advertisement
from app.schemas.ad import AdCreate, AdUpdate


class CRUDAd(CRUDBase[Advertisement, AdCreate, AdUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: AdCreate, owner_id: int
    ) -> Advertisement:
        """Create advertisement with current user."""
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


ad = CRUDAd(Advertisement)
