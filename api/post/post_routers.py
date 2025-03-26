from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.post.crud import crud_get_post, crud_get_all_posts, crud_create_post as crud_create_post, crud_update_post, crud_delete_post, crud_like_post
from api.post.schema import PostSchema, PostSchemaCreate, PostSchemaUpdate
from database import get_db
from models import Post
from fastapi_filter import FilterDepends, with_prefix
from api.post.post_filter import PostFilter
from sqlalchemy import select, func

router = APIRouter()

@router.post("/", response_model=PostSchema)
def create_post(post: PostSchemaCreate, user_id: int, db: Session = Depends(get_db)):
    return crud_create_post(db, post, user_id)

@router.get("/{post_id}", response_model=PostSchema)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud_get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return db_post

@router.get("/")
async def get_all_posts(
    db: Session = Depends(get_db),
    post_filter: PostFilter = FilterDepends(with_prefix("post", PostFilter), by_alias=True),
    page: int = 1,
    limit: int = 25,
):
    offset = (page - 1) * limit
    
    query = select(Post)
    query = post_filter.filter(query)

    total_query = select(func.count()).select_from(query.subquery())
    total = db.execute(total_query).scalar()
    
    query = query.offset(offset).limit(limit)
    result = db.execute(query)
  
    return {
        "posts": [PostSchema.from_orm(post) for post in result.scalars().all()],
        "total_objects": total,
        "page": page,
        "limit": limit
    }

@router.put("/{post_id}", response_model=PostSchema)
def update_post(post_id: int, post: PostSchemaUpdate, db: Session = Depends(get_db)):
    db_post = crud_update_post(db, post_id, post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return db_post

@router.delete("/{post_id}", response_model=PostSchema)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud_delete_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return db_post

@router.post("/{post_id}/like", response_model=PostSchema)
def like_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud_like_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return db_post