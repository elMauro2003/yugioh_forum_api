from sqlalchemy.orm import Session
from api.comment.schema import CommentSchemaUpdate,CommentSchemaCreate,CommentSchema
from api.post.crud import crud_get_post
from models import Comment


def crud_get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def crud_get_all_comments(db: Session, skip: int = 0, limit: int = 10):
    return CommentSchema[db.query(Comment).offset(skip).limit(limit).all()]

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