from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from auth import autenticar_usuario, verificar_codigo

router = APIRouter()

class AuthRequest(BaseModel):
    email: str

class VerifyRequest(BaseModel):
    email: str
    codigo: str

@router.post("/auth")
def authenticate_user(request: AuthRequest, db: Session = Depends(get_db)):
    usuario = autenticar_usuario(request.email, db)
    if usuario:
        return {"message": "Código enviado al usuario", "email": usuario.email}
    else:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")

@router.post("/verify")
def verify_code(request: VerifyRequest, db: Session = Depends(get_db)):
    if verificar_codigo(request.email, request.codigo, db):
        return {"message": "Autenticación exitosa"}
    else:
        raise HTTPException(status_code=400, detail="Código incorrecto")