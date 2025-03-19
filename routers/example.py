from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select, func
from typing import  Any,List, Optional
from sqlalchemy.orm import Session
from database import get_db
from filters.post_filter import PostFilter
from models import Post
from schemas import PostSchema
from fastapi_filter import FilterDepends, with_prefix
app = FastAPI()

class ItemSchema(BaseModel):
    id: int
    name: str
    description: str

router = APIRouter()

@router.get("/items")
async def get_items(
    db: Session = Depends(get_db),
    page: int = 1,
    limit: int = 25,
    name_filter: Optional[str] = None
):
    offset = (page - 1) * limit
    
    query = select(Post)
    
    if name_filter:
        query = query.where(Post.titulo.contains(name_filter))
        
    total_query = select(func.count()).select_from(query.subquery())
    total = db.execute(total_query).scalar()
    
    query = query.offset(offset).limit(limit)
    items = db.execute(query).scalars().all()
    
    return {
        "items": [PostSchema.from_orm(item) for item in items],
        "total": total,
        "page": page,
        "size": limit
    }
    
@router.get("/items_filter")
async def get_items_filter(
    db: Session = Depends(get_db),
    post_filter: PostFilter = FilterDepends(with_prefix("post", PostFilter), by_alias=True),
    page: int = 1,
    limit: int = 25,
):
    offset = (page - 1) * limit
    
    query = select(Post)
    query = post_filter.filter(query)

    total_query = select(func.count()).select_from(query.subquery())
    total = db.execute(total_query).scalar()
    
    query = query.offset(offset).limit(limit)
    result = db.execute(query)

    return {
        "posts": [PostSchema.from_orm(post) for post in result.scalars().all()],
        "total_objects": total,
        "page": page,
        "limit": limit
    }