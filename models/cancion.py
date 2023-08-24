from pydantic import BaseModel, Field
from typing import Optional

class Cancion(BaseModel):
    id: Optional[int] = None
    name: str = Field(default="Nueva canción", min_length=2, max_length=50)
    artista: str = Field(default="Nuevo artista", min_length=2, max_length=50)