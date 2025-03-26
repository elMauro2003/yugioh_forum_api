from pydantic import BaseModel, validator
import datetime
import enum

        
class UserSchema(BaseModel):
    id: int
    email: str
    
    class Config:
        orm_mode = True
        from_attributes = True

class CommentSchemaBase(BaseModel):
    description: str

class CommentSchemaCreate(CommentSchemaBase):
    pass

class CommentSchemaUpdate(CommentSchemaBase):
    pass

class CommentSchema(CommentSchemaBase):
    id: int
    likes: int
    create_at: datetime.datetime
    post_id: int
    user: UserSchema

    class Config:
        orm_mode = True
        from_attributes = True
