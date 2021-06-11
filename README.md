# lfd-todo
Test for Lyftron Data using FastAPI

install python3.8 from the source

create correct database connection string in database.py 

in alembic.ini change sqlalchemy.url with you correct database url like bellow
sqlalchemy.url = postgresql://ldf:ldf@localhost/lfdtodo

create virtual environment by using
virtualenv -p python3.8 venv

activate virtual environment

source virtuale_env_dir/venv/bin/activate

pip install -r requirements.txt

to create tables in database run this command 
alembic upgrade head

to run the server 

uvicorn main:app --reload

to run test

pytest test_main.py