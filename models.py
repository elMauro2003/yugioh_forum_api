from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum
import datetime

class PostType(enum.Enum):
    Reporte = "Reporte"
    Sugerencia = "Sugerencia"
    Comentario = "Comentario"

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    codigo = Column(String, index=True)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    fecha_creacion = Column(DateTime, default=datetime.datetime.utcnow)
    tipo = Column(Enum(PostType))
    descripcion = Column(String)
    likes = Column(Integer, default=0)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="posts")

class Comentario(Base):
    __tablename__ = "comentarios"
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)
    likes = Column(Integer, default=0)
    post_id = Column(Integer, ForeignKey("posts.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    post = relationship("Post", back_populates="comentarios")
    usuario = relationship("Usuario", back_populates="comentarios")

Usuario.posts = relationship("Post", back_populates="usuario")
Usuario.comentarios = relationship("Comentario", back_populates="usuario")
Post.comentarios = relationship("Comentario", back_populates="post")