from pydantic import BaseModel, validator
from typing import List, Optional
import datetime
import enum
from schemas import Comentario


class PostCategory(str, enum.Enum):
    Actualitation = "Actualitation"
    Event = "Event"
    Vote = "Vote"
    Error = "Error"


class PostType(str, enum.Enum):
    Reporte = "Reporte"
    Sugerencia = "Sugerencia"
    Comentario = "Comentario"

class PostSchemaBase(BaseModel):
    titulo: str
    tipo: PostType
    category: PostCategory
    descripcion: str

class PostSchemaCreate(PostSchemaBase):
    pass

class PostSchemaUpdate(PostSchemaBase):
    pass

class PostSchema(PostSchemaBase):
    id: int
    fecha_creacion: datetime.datetime
    likes: int
    usuario_id: int
    comentarios: List['Comentario'] = []
    total_comments: int

    class Config:
        orm_mode = True
        from_attributes = True
        
    # Validador para calcular la cantidad de comentarios
    # @validator('total_comments', always=True)
    # def calcular_total_comments(cls, v, values):
    #     return len(values.get('comentarios', [])) or 0