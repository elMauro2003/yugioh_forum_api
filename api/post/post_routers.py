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
from datetime import datetime
from auth import get_actual_user

router = APIRouter()

@router.post("/")
def create_post(post: PostSchemaCreate, db: Session = Depends(get_db), userPermission=Depends(get_actual_user)): #
    # Crear un nuevo post asociado al usuario autenticado
    nuevo_post = Post(
        title=post.title,
        category=post.category, 
        slug = f"{post.title.replace(' ', '-').lower()}-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}", # Generar un slug único
        description=post.description,
        user_id = userPermission.id, # Obtener el ID del usuario autenticado
        create_date_at=datetime.today(),
        create_time_at=datetime.now().time()
    )
    db.add(nuevo_post)
    db.commit()
    db.refresh(nuevo_post)
    return nuevo_post

@router.get("/{post_slug}", response_model=PostSchema)
def read_post(post_slug: str, db: Session = Depends(get_db)):
    db_post = crud_get_post(db, post_slug)
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
def update_post(post_id: int, post: PostSchemaUpdate, db: Session = Depends(get_db), userPermission=Depends(get_actual_user)):
    db_post = crud_update_post(db, post_id, post, userPermission.id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return db_post

@router.delete("/{post_id}", response_model=PostSchema)
def delete_post(post_id: int, db: Session = Depends(get_db), userPermission=Depends(get_actual_user)):
    db_post = crud_delete_post(db, post_id,userPermission.id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return db_post

@router.post("/{post_id}/like", response_model=PostSchema)
def like_post(post_id: int, db: Session = Depends(get_db), userPermission=Depends(get_actual_user)):
    db_post = crud_like_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return db_post