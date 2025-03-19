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
        codigo = generar_codigo()
        usuario.codigo = codigo
        db.commit()
        db.refresh(usuario)
        print(f"Código de verificación para {email}: {codigo}")  # Solo para pruebas
        return usuario
    else:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    
    
def verificar_codigo(email: str, codigo: str, db: Session):
    usuario = db.query(Usuario).filter(Usuario.email == email, Usuario.codigo == codigo).first()
    if usuario:
        return True
    else:
        return False