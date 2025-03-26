from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum
import datetime
from pydantic import BaseModel

class PostCategory(enum.Enum):
    Actualitation = "Actualitation"
    Event = "Event"
    Vote = "Vote"
    Error = "Error"


class PostType(enum.Enum):
    Report = "Report"
    Suggestion = "Suggestion"
    Comment = "Comment"
    
class PostSchemaCreate(BaseModel):
    title: str
    type: PostType
    category: PostCategory
    description: str

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    code = Column(String, index=True)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    create_at = Column(DateTime, default=datetime.datetime.utcnow)
    type = Column(Enum(PostType))
    category = Column(Enum(PostCategory))
    description = Column(String)
    likes = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="posts")

        
        
class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    likes = Column(Integer, default=0)
    create_at = Column(DateTime, default=datetime.datetime.utcnow)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    post = relationship("Post", back_populates="comments")
    user = relationship("User", back_populates="comments")

User.posts = relationship("Post", back_populates="user")
User.comments = relationship("Comment", back_populates="user")
Post.comments = relationship("Comment", back_populates="post")