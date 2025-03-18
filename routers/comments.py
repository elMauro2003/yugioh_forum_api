from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud import get_comentario, get_comentarios, create_comentario, update_comentario, delete_comentario, like_comentario
from schemas import Comentario, ComentarioCreate, ComentarioUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=Comentario)
def create_comment(comentario: ComentarioCreate, post_id: int, usuario_id: int, db: Session = Depends(get_db)):
    return create_comentario(db, comentario, post_id, usuario_id)

@router.get("/{comentario_id}", response_model=Comentario)
def read_comment(comentario_id: int, db: Session = Depends(get_db)):
    db_comentario = get_comentario(db, comentario_id)
    if db_comentario is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comentario

@router.get("/", response_model=List[Comentario])
def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    comentarios = get_comentarios(db, skip=skip, limit=limit)
    return comentarios

@router.put("/{comentario_id}", response_model=Comentario)
def update_comment(comentario_id: int, comentario: ComentarioUpdate, db: Session = Depends(get_db)):
    db_comentario = update_comentario(db, comentario_id, comentario)
    if db_comentario is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comentario

@router.delete("/{comentario_id}", response_model=Comentario)
def delete_comment(comentario_id: int, db: Session = Depends(get_db)):
    db_comentario = delete_comentario(db, comentario_id)
    if db_comentario is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comentario

@router.post("/{comentario_id}/like", response_model=Comentario)
def like_comment(comentario_id: int, db: Session = Depends(get_db)):
    db_comentario = like_comentario(db, comentario_id)
    if db_comentario is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return db_comentario