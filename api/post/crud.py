from sqlalchemy.orm import Session
from models import Post
from schemas import PostSchemaCreate, PostSchemaUpdate


def crud_get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def crud_get_all_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def crud_create_post(db: Session, post: PostSchemaCreate, usuario_id: int):
    db_post = Post(**post.dict(), usuario_id=usuario_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def crud_update_post(db: Session, post_id: int, post: PostSchemaUpdate):
    db_post = crud_get_post(db, post_id)
    if db_post:
        db_post.titulo = post.titulo
        db_post.tipo = post.tipo
        db_post.descripcion = post.descripcion
        db.commit()
        db.refresh(db_post)
        return db_post
    return None

def crud_delete_post(db: Session, post_id: int):
    db_post = crud_get_post(db, post_id)
    if db_post:
        db.delete(db_post)
        db.commit()
        return db_post
    return None

def crud_like_post(db: Session, post_id: int):
    db_post = crud_get_post(db, post_id)
    if db_post:
        db_post.likes += 1
        db.commit()
        db.refresh(db_post)
        return db_post
    return None