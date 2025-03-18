from fastapi import FastAPI
from database import engine, Base
from routers import users, posts, comments

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])