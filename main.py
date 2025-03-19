from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import users, posts, comments, auth_user
from decouple import config

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuración de CORS
LIST_ALLOWED_HOSTS = config('ALLOWED_HOSTS',default='*')
ALLOWED_HOSTS = LIST_ALLOWED_HOSTS.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])
app.include_router(auth_user.router, prefix="/auth", tags=["auth"])