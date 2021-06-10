from pydantic import BaseModel
from typing import Optional

class ToDo(BaseModel):
    title: str
    description: str

class ShowTodo(BaseModel):
    # title: str
    # description: str
    class Config():
        orm_mode = True
