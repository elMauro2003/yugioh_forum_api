from pydantic import BaseModel, validator
from typing import List, Optional
import datetime
import enum

        
class UserSchema(BaseModel):
    id: int
    email: str
    
    class Config:
        orm_mode = True
        from_attributes = True

class PostCategory(str, enum.Enum):
    Actualitation = "Actualitation"
    Event = "Event"
    Vote = "Vote"
    Error = "Error"


class PostType(str, enum.Enum):
    Report = "Report"
    Suggestion = "Suggestion"
    Comment = "Comment"

class PostSchemaBase(BaseModel):
    title: str
    type: PostType
    category: PostCategory
    description: str

class PostSchemaCreate(PostSchemaBase):
    pass

class PostSchemaUpdate(PostSchemaBase):
    pass

class PostSchema(PostSchemaBase):
    id: int
    create_at: datetime.datetime
    likes: int
    user: UserSchema
    comments: List['CommentSchema'] = []
    total_comments: int = 0

    class Config:
        orm_mode = True
        from_attributes = True
        
    # Calculate total comments relations
    @validator('total_comments', always=True)
    def calcular_total_comments(cls, v, values):
        return len(values.get('comments', [])) or 0
    

class CommentSchema(BaseModel):
    id: int
    likes: int
    create_at: datetime.datetime
    description: str
    user: UserSchema

    class Config:
        orm_mode = True
        from_attributes = True
