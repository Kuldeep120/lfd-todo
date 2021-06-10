from pydantic import BaseModel
from typing import Optional

class ToDo(BaseModel):
    title: str
    description: str
