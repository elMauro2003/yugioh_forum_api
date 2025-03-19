from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud import get_post, get_posts, create_post as crud_create_post, update_post, delete_post, like_post
from schemas import Post, PostCreate, PostUpdate
from database import get_db
from auth import obtener_usuario_actual

router = APIRouter()

# @router.post("/", response_model=Post)
# def create_post(post: PostCreate, db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
#     return crud_create_post(db, post, usuario.id)

# @router.get("/{post_id}", response_model=Post)
# def read_post(post_id: int, db: Session = Depends(get_db)):
#     db_post = get_post(db, post_id)
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post no encontrado")
#     return db_post


@router.post("/", response_model=Post)
def create_post(post: PostCreate, db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    # El usuario autenticado está disponible como "usuario"
    return crud_create_post(db, post, usuario.id)

@router.get("/", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), usuario=Depends(obtener_usuario_actual)):
    # Solo usuarios autenticados pueden acceder a esta ruta
    return get_posts(db, skip=skip, limit=limit)

@router.get("/", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = get_posts(db, skip=skip, limit=limit)
    return posts

@router.put("/{post_id}", response_model=Post)
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    db_post = update_post(db, post_id, post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return db_post

@router.delete("/{post_id}", response_model=Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = delete_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return db_post

@router.post("/{post_id}/like", response_model=Post)
def like_post(post_id: int, db: Session = Depends(get_db)):
    db_post = like_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return db_post