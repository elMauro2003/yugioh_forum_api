from sqlalchemy.orm import Session
from models import Post
from api.post.schema import PostSchemaCreate, PostSchemaUpdate


def crud_get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def crud_get_all_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def crud_create_post(db: Session, post: PostSchemaCreate, user_id: int):
    db_post = Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def crud_update_post(db: Session, post_id: int, post: PostSchemaUpdate, user_id: int):
    db_post = crud_get_post(db, post_id)
    if db_post and db_post.user_id == user_id:
        db_post.title = post.title
        db_post.description = post.description
        db.commit()
        db.refresh(db_post)
        return db_post
    return None

def crud_delete_post(db: Session, post_id: int,user_id: int):
    db_post = crud_get_post(db, post_id)
    if db_post and db_post.user_id == user_id:
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