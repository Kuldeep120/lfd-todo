from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)