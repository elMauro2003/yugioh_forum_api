from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud import get_usuario, get_usuarios, create_usuario, update_usuario, delete_usuario
from schemas import Usuario, UsuarioCreate, UsuarioUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=Usuario)
def create_user(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return create_usuario(db, usuario)

@router.get("/{usuario_id}", response_model=Usuario)
def read_user(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.get("/", response_model=List[Usuario])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    usuarios = get_usuarios(db, skip=skip, limit=limit)
    return usuarios

@router.put("/{usuario_id}", response_model=Usuario)
def update_user(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    db_usuario = update_usuario(db, usuario_id, usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.delete("/{usuario_id}", response_model=Usuario)
def delete_user(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = delete_usuario(db, usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario