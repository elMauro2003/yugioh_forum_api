from typing import Optional
from fastapi_filter.contrib.sqlalchemy import Filter
from fastapi_filter import FilterDepends, with_prefix
import enum
from sqlalchemy import  Enum
from models import Post


class PostCategory(str, enum.Enum):
    Actualitation = "Actualitation"
    Event = "Event"
    Vote = "Vote"
    Error = "Error"


class PostType(str, enum.Enum):
    Report = "Report"
    Suggestion = "Suggestion"
    Comment = "Comment"


class PostFilter(Filter):
    title__ilike: Optional[str]= None
    type : Optional[str] = None
    category : Optional[str] = None
    description__ilike: Optional[str]= None
    order_by: Optional[list[str]] = None
    
    class Constants(Filter.Constants):
        model = Post
        search_model_fields = ["title", "description"]
