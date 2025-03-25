from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from auth import autenticated_user, auth_verify_code, check_token, create_access_token, create_refresh_token, verify_token
from schemas import Token
from jose import JWTError


router = APIRouter()

class AuthRequest(BaseModel):
    email: str

class VerifyRequest(BaseModel):
    email: str
    code: str
    
class RefreshRequest(BaseModel):
    refresh_token: str

@router.post("/auth")
def authenticate_user(request: AuthRequest, db: Session = Depends(get_db)):
    user = autenticated_user(request.email, db)
    if user:
        return {"message": "Código enviado al usuario", "email": user.email, "code": user.code }
    else:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")

# @router.post("/verify")
# def verify_code(request: VerifyRequest, db: Session = Depends(get_db)):
#     if verify_code(request.email, request.code, db):
#         # Crear un token JWT
#         token = create_access_token({"sub": request.email})
#         return {"message": "Autenticación exitosa"}
#     else:
#         raise HTTPException(status_code=400, detail="Código incorrecto")

@router.post("/verify")
def verify_code(request: VerifyRequest, db: Session = Depends(get_db)):
    if auth_verify_code(request.email, request.code, db):
        # Crear tokens
        access_token = create_access_token({"sub": request.email})
        refresh_token = create_refresh_token({"sub": request.email})
        return {
            "user_email": request.email,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    else:
        raise HTTPException(status_code=400, detail="Código incorrecto")

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = autenticated_user(form_data.username, db)
    if not usuario:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    token = create_access_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/refresh")
def refresh_token(request: RefreshRequest):
    try:
        # Verificar el token de actualización
        payload = verify_token(request.refresh_token)
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        # Crear un nuevo token de acceso
        access_token = create_access_token({"sub": email})
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    except JWTError:
        raise HTTPException(status_code=401, detail="Token de actualización inválido o expirado")