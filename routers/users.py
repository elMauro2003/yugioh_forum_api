from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud import crud_get_user, crud_get_all_users, crud_create_user, crud_update_user, crud_delete_user
from schemas import UserSchema, UserSchemaCreate, UserSchemaUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=UserSchema)
def create_user(user: UserSchemaCreate, db: Session = Depends(get_db)):
    return crud_create_user(db, user)

@router.get("/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@router.get("/", response_model=List[UserSchema])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud_get_all_users(db, skip=skip, limit=limit)
    return users

@router.put("/{user_id}", response_model=UserSchema)
def update_user(user_id: int, usuario: UserSchemaUpdate, db: Session = Depends(get_db)):
    db_user = crud_update_user(db, user_id, usuario)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@router.delete("/{user_id}", response_model=UserSchema)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user