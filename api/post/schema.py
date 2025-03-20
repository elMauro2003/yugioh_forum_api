from pydantic import BaseModel, validator
from typing import List, Optional
import datetime
import enum

# from schemas import SchemaComment


# from schemas import Comentario


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
    user_id: int
    # comentarios: List['SchemaComment'] = []
    # total_comments: int

    class Config:
        orm_mode = True
        from_attributes = True
        
    # Validador para calcular la cantidad de comentarios
    # @validator('total_comments', always=True)
    # def calcular_total_comments(cls, v, values):
    #     return len(values.get('comentarios', [])) or 0