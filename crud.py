from sqlalchemy.orm import Session
from api.post.crud import crud_get_post
from models import User, Post, Comment
from schemas import  UserSchemaCreate, UserSchemaUpdate, CommentSchemaCreate, CommentSchemaUpdate


def crud_get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def crud_get_all_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def crud_create_user(db: Session, user: UserSchemaCreate):
    db_user = User(email=user.email)
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


def crud_get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
