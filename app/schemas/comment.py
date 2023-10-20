from typing import Optional
import datetime

from pydantic import BaseModel, ConfigDict


class CommentBase(BaseModel):
    description: Optional[str] = None


class CommentCreate(CommentBase):
    description: str


class CommentUpdate(CommentCreate):
    pass


class CommentInDBBase(CommentBase):
    id: int
    ad_id: int
    author_id: int
    pub_date: datetime.datetime

    model_config = ConfigDict(from_attributes=True)


class Comment(CommentInDBBase):
    pass
