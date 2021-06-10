from fastapi import FastAPI, Depends, status, Response, HTTPException
from todo import schema 
from todo import models 
from todo.database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
# from os.path import dirname, realpath, sep, pardir
# import sys
# sys.path.append(dirname(realpath(__file__)) + sep + pardir + sep + "lib")
models.Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/todo/', status_code = status.HTTP_201_CREATED)
def create_todo(todo: schema.ToDo, db: Session = Depends(get_db)):
    new_todo = models.Todo(title = todo.title, description = todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@app.delete('/todo/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_todo(id: int, db: Session = Depends(get_db)):
    # todo = db.query(models.Todo).fitler(models.Todo.id == id).first()
    db.query(models.Todo).filter(models.Todo.id == id).delete()
    db.commit()
    return {'detail': 'Successfully delete the todo item'}


@app.get('/todo/{id}', status_code = status.HTTP_200_OK)
def get_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    return todo


@app.put('/todo/{id}', status_code = status.HTTP_202_ACCEPTED)
def update_todo(id: int, todo: schema.ToDo, db: Session = Depends(get_db)):
    update_todo = db.query(models.Todo).filter(models.Todo.id == id)

    if not todo:
        raise HTTPException(status_code=404, detail="Item not found")

    update_todo.update(todo.dict())
    db.commit()
    return {'detail':'success'}

# @app.get('/todo/', response_model=List[schema.ShowTodo])
@app.get('/todo/')
def list_todo(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = db.query(models.Todo).offset(skip).limit(limit).all()
    return todos
