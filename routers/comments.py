from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud import crud_get_comment, crud_get_all_comments, crud_create_comment, crud_update_comment, crud_delete_comment, crud_like_comment
from schemas import CommentSchema, CommentSchemaCreate, CommentSchemaUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=CommentSchema)
def create_comment(comment: CommentSchemaCreate, post_id: int, user_id: int, db: Session = Depends(get_db)):
    return crud_create_comment(db, comment, post_id, user_id)

@router.get("/{comment_id}", response_model=CommentSchema)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud_get_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comment

@router.get("/", response_model=List[CommentSchema])
def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    comments = crud_get_all_comments(db, skip=skip, limit=limit)
    return comments

@router.put("/{comment_id}", response_model=CommentSchema)
def update_comment(comment_id: int, comment: CommentSchemaUpdate, db: Session = Depends(get_db)):
    db_comment = crud_update_comment(db, comment_id, comment)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comment

@router.delete("/{comment_id}", response_model=CommentSchema)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud_delete_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comment

@router.post("/{comment_id}/like", response_model=CommentSchema)
def like_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud_like_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comment