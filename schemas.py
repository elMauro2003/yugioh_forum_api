from pydantic import BaseModel
from typing import List, Optional
import datetime
import enum

class Token(BaseModel):
    access_token: str
    token_type: str

class PostType(str, enum.Enum):
    Reporte = "Reporte"
    Sugerencia = "Sugerencia"
    Comentario = "Comentario"

class UsuarioBase(BaseModel):
    email: str

class UsuarioCreate(UsuarioBase):
    codigo: str

class UsuarioUpdate(UsuarioBase):
    codigo: str

class Usuario(UsuarioBase):
    id: int
    posts: List['Post'] = []
    comentarios: List['Comentario'] = []

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    titulo: str
    tipo: PostType
    descripcion: str

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int
    fecha_creacion: datetime.datetime
    likes: int
    usuario_id: int
    comentarios: List['Comentario'] = []

    class Config:
        orm_mode = True

class ComentarioBase(BaseModel):
    descripcion: str

class ComentarioCreate(ComentarioBase):
    pass

class ComentarioUpdate(ComentarioBase):
    pass

class Comentario(ComentarioBase):
    id: int
    likes: int
    post_id: int
    usuario_id: int

    class Config:
        orm_mode = True
