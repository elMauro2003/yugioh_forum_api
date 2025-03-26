from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.send_email.email_template import render_email_template
from database import get_db
from auth import autenticated_user, auth_verify_code, check_token, create_access_token, create_refresh_token, verify_token
from schemas import Token
from jose import JWTError
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

conf = ConnectionConfig(
    MAIL_USERNAME="zona0django@gmail.com",
    MAIL_PASSWORD="lcof vchy ajnd osbh",
    MAIL_FROM="zona0django@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,  
    MAIL_SSL_TLS=False,  
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

router = APIRouter()

class AuthRequest(BaseModel):
    email: str

class VerifyRequest(BaseModel):
    email: str
    code: str
    
class RefreshRequest(BaseModel):
    refresh_token: str

@router.post("/auth")
async def authenticate_user(request: AuthRequest, db: Session = Depends(get_db)):
    user = autenticated_user(request.email, db)
    if user:
        html_content = render_email_template('welcome.html', {"email":user.email,"code":user.code})
        message = MessageSchema(
            subject=f"Hola {user.email}",
            recipients=[user.email],
            body=html_content,
            subtype="html"
        )
        fm = FastMail(conf)
        await fm.send_message(message)
        return {"message": "Código enviado al usuario", "email": user.email }
    else:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")

@router.post("/verify")
def verify_code(request: VerifyRequest, db: Session = Depends(get_db)):
    if auth_verify_code(request.email, request.code, db):
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
    user = autenticated_user(form_data.username, db)
    if not user:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/refresh")
def refresh_token(request: RefreshRequest):
    try:
     
        payload = verify_token(request.refresh_token)
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")

       
        access_token = create_access_token({"sub": email})
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    except JWTError:
        raise HTTPException(status_code=401, detail="Token de actualización inválido o expirado")