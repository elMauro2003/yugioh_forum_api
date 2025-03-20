from pydantic import BaseModel, validator
from typing import List, Optional
import datetime
import enum
from api.post.schema import PostSchema

class Token(BaseModel):
    access_token: str
    token_type: str



class UserSchemaBase(BaseModel):
    email: str

class UserSchemaCreate(UserSchemaBase):
    codigo: str

class UserSchemaUpdate(UserSchemaBase):
    codigo: str

class UserSchema(UserSchemaBase):
    id: int
    posts: List['PostSchema'] = []
    comentarios: List['CommentSchema'] = []

    class Config:
        orm_mode = True



class CommentSchemaBase(BaseModel):
    description: str

class CommentSchemaCreate(CommentSchemaBase):
    pass

class CommentSchemaUpdate(CommentSchemaBase):
    pass

class CommentSchema(CommentSchemaBase):
    id: int
    likes: int
    post_id: int
    user_id: int

    class Config:
        orm_mode = True
