from fastapi import APIRouter, FastAPI, Depends, status, Response, HTTPException
from todo import schema 
from . import crud
from database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    tags = ['Todos']
    )

@router.get('/todo/')
def list_todo(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all(skip, limit, db)

@router.post('/todo/', status_code = status.HTTP_201_CREATED)
def create_todo(todo: schema.ToDo, db: Session = Depends(get_db)):
    return crud.create(todo, db)

@router.get('/todo/{id}', status_code = status.HTTP_200_OK)
def get_todo(id: int, db: Session = Depends(get_db)):
    return crud.read(id, db)

@router.put('/todo/{id}', status_code = status.HTTP_202_ACCEPTED)
def update_todo(id: int, todo: schema.ToDo, db: Session = Depends(get_db)):
    return crud.update(id, todo, db)

@router.delete('/todo/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_todo(id: int, db: Session = Depends(get_db)):
    crud.delete(id, db)