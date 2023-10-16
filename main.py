from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from schem.schemas import Ques
from db import engine, get_db, Base

import crud


Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post('/')
def post(qu: Ques,db: Session = Depends(get_db)):
    return crud.creat_user(qu,db)


@app.get('/get')
def show(db: Session = Depends(get_db)):
    return crud.show(db)