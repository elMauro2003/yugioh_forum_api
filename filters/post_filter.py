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
    Reporte = "Reporte"
    Sugerencia = "Sugerencia"
    Comentario = "Comentario"


class PostFilter(Filter):
    titulo__ilike: Optional[str]= None
    tipo : Optional[str] = None
    category : Optional[str] = None
    descripcion__ilike: Optional[str]= None
    order_by: Optional[list[str]] = None
    
    class Constants(Filter.Constants):
        model = Post
        search_model_fields = ["titulo", "descripcion"]
