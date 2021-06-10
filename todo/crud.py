from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from . import schema as Schema
from . import models

def get_all(skip: int, limit: int, db: Session) :
    todos = db.query(models.Todo).offset(skip).limit(limit).all()
    return todos

def create(todo: Schema.ToDo, db: Session):
    new_todo = models.Todo(title = todo.title, description = todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def read(id: int, db: Session):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
         detail = "Record with id %s not found" %id)
    return todo

def update(id: int, todo: Schema.ToDo, db: Session):
    update_todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not update_todo.count():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail = "Record with id %s not found" %id)

    update_todo.update(todo.dict())
    db.commit()
    return {'detail':'success'}

def delete(id: int, db: Session):
    todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo.count():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail = "Record with id %s not found" %id)
    todo.delete()
    db.commit()
    return {'detail': 'Successfully delete the todo item'}