from sqlalchemy.orm import Session
from api.post.crud import crud_get_post
from models import User, Post, Comment
from schemas import  UserSchemaCreate, UserSchemaUpdate, CommentSchemaCreate, CommentSchemaUpdate


def crud_get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def crud_get_all_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def crud_create_user(db: Session, user: UserSchemaCreate):
    db_user = User(email=user.email, code=user.code)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def crud_update_user(db: Session, user_id: int, user: UserSchemaUpdate):
    db_user = crud_get_user(db, user_id)
    if db_user:
        db_user.email = user.email
        db_user.code = user.code
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def crud_delete_user(db: Session, user_id: int):
    db_user = crud_get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None





def crud_get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def crud_get_all_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Comment).offset(skip).limit(limit).all()

def crud_create_comment(db: Session, comment: CommentSchemaCreate, post_id: int, user_id: int):
    db_comment = Comment(**comment.dict(), post_id=post_id, user_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def crud_update_comment(db: Session, comment_id: int, comment: CommentSchemaUpdate):
    db_comment = crud_get_comment(db, comment_id)
    if db_comment:
        db_comment.descripcion = comment.descripcion
        db.commit()
        db.refresh(db_comment)
        return db_comment
    return None

def crud_delete_comment(db: Session, comment_id: int):
    db_comment = crud_get_all_comments(db, comment_id)
    if db_comment:
        db.delete(db_comment)
        db.commit()
        return db_comment
    return None


def crud_like_post(db: Session, post_id: int):
    db_post = crud_get_post(db, post_id)
    if db_post:
        db_post.likes += 1
        db.commit()
        db.refresh(db_post)
        return db_post
    return None

def crud_like_comment(db: Session, comment_id: int):
    db_comment = crud_get_comment(db, comment_id)
    if db_comment:
        db_comment.likes += 1
        db.commit()
        db.refresh(db_comment)
        return db_comment
    return None