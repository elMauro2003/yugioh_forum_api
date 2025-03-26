from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.comment.crud import crud_get_comment, crud_create_comment, crud_update_comment, crud_delete_comment, crud_like_comment
from models import Comment
from api.comment.schema import CommentSchema, CommentSchemaCreate, CommentSchemaUpdate
from database import get_db
from api.comment.comment_filter import CommentFilter
from sqlalchemy import select, func
from fastapi_filter import FilterDepends, with_prefix
from auth import get_actual_user

router = APIRouter()

@router.post("/", response_model=CommentSchema)
def create_comment(comment: CommentSchemaCreate, post_id: int, user_id: int, db: Session = Depends(get_db), usuario=Depends(get_actual_user)):
    return crud_create_comment(db, comment, post_id, user_id)

@router.get("/{comment_id}", response_model=CommentSchema)
def read_comment(comment_id: int, db: Session = Depends(get_db), usuario=Depends(get_actual_user)):
    db_comment = crud_get_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comment

@router.get("/")
async def get_all_comments(
    db: Session = Depends(get_db), usuario=Depends(get_actual_user),
    comment_filter: CommentFilter = FilterDepends(with_prefix("comment", CommentFilter), by_alias=True),
    page: int = 1,
    limit: int = 25,
):
    offset = (page - 1) * limit
    
    query = select(Comment)
    query = comment_filter.filter(query)
    query = comment_filter.sort(query)

    total_query = select(func.count()).select_from(query.subquery())
    total = db.execute(total_query).scalar()
    
    query = query.offset(offset).limit(limit)
    result = db.execute(query)
  
    return {
        "comments": [CommentSchema.from_orm(comment) for comment in result.scalars().all()],
        "total_objects": total,
        "page": page,
        "limit": limit
    }

@router.put("/{comment_id}", response_model=CommentSchema)
def update_comment(comment_id: int, comment: CommentSchemaUpdate, db: Session = Depends(get_db), usuario=Depends(get_actual_user)):
    db_comment = crud_update_comment(db, comment_id, comment)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comment

@router.delete("/{comment_id}", response_model=CommentSchema)
def delete_comment(comment_id: int, db: Session = Depends(get_db), usuario=Depends(get_actual_user)):
    db_comment = crud_delete_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comment

@router.post("/{comment_id}/like", response_model=CommentSchema)
def like_comment(comment_id: int, db: Session = Depends(get_db), usuario=Depends(get_actual_user)):
    db_comment = crud_like_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comment