from sqlalchemy.orm import Session
from models import Usuario, Post, Comentario
from schemas import  UsuarioCreate, UsuarioUpdate, ComentarioCreate, ComentarioUpdate


def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Usuario).offset(skip).limit(limit).all()

def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(email=usuario.email, codigo=usuario.codigo)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: UsuarioUpdate):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        db_usuario.email = usuario.email
        db_usuario.codigo = usuario.codigo
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    return None

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
        return db_usuario
    return None





def get_comentario(db: Session, comentario_id: int):
    return db.query(Comentario).filter(Comentario.id == comentario_id).first()

def get_comentarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Comentario).offset(skip).limit(limit).all()

def create_comentario(db: Session, comentario: ComentarioCreate, post_id: int, usuario_id: int):
    db_comentario = Comentario(**comentario.dict(), post_id=post_id, usuario_id=usuario_id)
    db.add(db_comentario)
    db.commit()
    db.refresh(db_comentario)
    return db_comentario

def update_comentario(db: Session, comentario_id: int, comentario: ComentarioUpdate):
    db_comentario = get_comentario(db, comentario_id)
    if db_comentario:
        db_comentario.descripcion = comentario.descripcion
        db.commit()
        db.refresh(db_comentario)
        return db_comentario
    return None

def delete_comentario(db: Session, comentario_id: int):
    db_comentario = get_comentario(db, comentario_id)
    if db_comentario:
        db.delete(db_comentario)
        db.commit()
        return db_comentario
    return None


def like_post(db: Session, post_id: int):
    db_post = get_post(db, post_id)
    if db_post:
        db_post.likes += 1
        db.commit()
        db.refresh(db_post)
        return db_post
    return None

def like_comentario(db: Session, comentario_id: int):
    db_comentario = get_comentario(db, comentario_id)
    if db_comentario:
        db_comentario.likes += 1
        db.commit()
        db.refresh(db_comentario)
        return db_comentario
    return None