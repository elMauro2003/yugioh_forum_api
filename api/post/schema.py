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

class PostSchemaBase(BaseModel):
    title: str
    category: PostCategory
    description: str
    

class PostSchemaCreate(PostSchemaBase):
    pass

class PostSchemaUpdate(PostSchemaBase):
    pass

class PostSchema(PostSchemaBase):
    id: int
    slug : str
    create_date_at: datetime.date
    create_time_at: datetime.time
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
    create_date_at: datetime.date
    create_time_at: datetime.time
    description: str
    user: UserSchema

    class Config:
        orm_mode = True
        from_attributes = True
