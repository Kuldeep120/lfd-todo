from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return 'Hello World'

@app.post('/todo')
def create_todo():
    pass

@app.delete('/todo/{id}')
def delete_todo(id: int):
    pass

@app.get('/todo/{id}')
def get_todo(id: int):
    pass

@app.put('/todo/{id}')
def update_todo(id: int):
    pass

@app.put('/todo/list')
def list_todo():
    pass
