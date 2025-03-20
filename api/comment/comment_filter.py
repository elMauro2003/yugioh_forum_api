from typing import Optional
from fastapi_filter.contrib.sqlalchemy import Filter
from fastapi_filter import FilterDepends, with_prefix
import enum
from sqlalchemy import  Enum
from models import Comment


class CommentFilter(Filter):
    post_id: Optional[int]= None
    order_by: Optional[list[str]] = ["-create_at"]
    
    class Constants(Filter.Constants):
        model = Comment

