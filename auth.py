import random
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from schemas import UsuarioCreate
from datetime import datetime, timedelta
from jose import JWTError, jwt
from decouple import config
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

# OAuth2PasswordBearer para obtener el token del encabezado Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

# Configuración de JWT
SECRET_KEY = config("SECRET_KEY", default="secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15  # Duración del token de acceso (en minutos)
REFRESH_TOKEN_EXPIRE_DAYS = 7     # Duración del token de actualización (en días)

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
    
    
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

def check_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return email
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    
    

# def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     email = check_token(token)
#     usuario = db.query(Usuario).filter(Usuario.email == email).first()
#     if usuario is None:
#         raise HTTPException(status_code=401, detail="Usuario no encontrado")
#     return usuario

def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        # Decodificar el token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        
        # Buscar el usuario en la base de datos
        usuario = db.query(Usuario).filter(Usuario.email == email).first()
        if usuario is None:
            raise HTTPException(status_code=401, detail="Usuario no encontrado")
        return usuario
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")