from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Comment
from app.schemas.comment import CommentCreate, CommentUpdate


class CRUDComment(CRUDBase[Comment, CommentCreate, CommentUpdate]):
    def create_new_comment(
        self, db: Session, *, obj_in: CommentCreate, author_id: int, ad_id: int
    ) -> Comment:
        """Create comment with current user on ad."""
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, author_id=author_id, ad_id=ad_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


comment = CRUDComment(Comment)
