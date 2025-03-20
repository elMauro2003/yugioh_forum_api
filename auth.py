import random
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from datetime import datetime, timedelta
from jose import JWTError, jwt
from decouple import config
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

# OAuth2PasswordBearer para obtener el token del encabezado Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

# Configuración de JWT
SECRET_KEY = config("SECRET_KEY", default="secret_key")  # Cambia esto en producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15  # Duración del token de acceso (en minutos)
REFRESH_TOKEN_EXPIRE_DAYS = 7     # Duración del token de actualización (en días)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_code():
    return str(random.randint(100000, 999999))


def autenticated_user(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if user:
        code = generate_code()
        user.code = code
        db.commit()
        db.refresh(user)
        return user
    else:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    
    
def verify_code(email: str, code: str, db: Session):
    user = db.query(User).filter(User.email == email, User.code == code).first()
    if user:
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

def get_actual_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        # Decodificar el token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        
        # Buscar el usuario en la base de datos
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=401, detail="Usuario no encontrado")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")