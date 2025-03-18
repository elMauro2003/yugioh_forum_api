import random
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from schemas import UsuarioCreate

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generar_codigo():
    return str(random.randint(100000, 999999))

def autenticar_usuario(email: str, db: Session):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        usuario.codigo = generar_codigo()
        db.commit()
        db.refresh(usuario)
        return usuario
    else:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")