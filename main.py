from os.path import dirname, realpath, sep, pardir
import sys
sys.path.append(dirname(realpath(__file__)) )

from fastapi import FastAPI

from todo import router as todo_router

app = FastAPI()

app.include_router(todo_router.router)
