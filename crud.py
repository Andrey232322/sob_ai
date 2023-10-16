import requests
from fastapi import Depends

from db import get_db
from model.model import Ques
from sqlalchemy.orm import Session
from schem import schemas




def pars():
    BASE_URL = 'https://jservice.io/api/random?count=1'

    response = requests.get(f"{BASE_URL}")
    a = response.json()
    w = {}
    for i in a:
        w = i
    return w
def creat_user(data: schemas.Ques,db):
    a = pars()
    a['id']
    data.id = a['id']
    data.question = a['question']
    data.answer = a['answer']
    #data.created_at = a['created_at']
    ques = Ques(id=data.id, question=data.question, answer=data.answer, created_at=data.created_at)
    #ques = Ques(id=data.id ,question= data.question,answer= data.answer,created_at= data.created_at)
    try:
        db.add(ques)
        db.commit()
        db.refresh(ques)
    except Exception as e:
        print(e)
    return ques


def show(db):
    return db.query(Ques).order_by(Ques.created_at.desc()).first()















# BASE_URL = 'https://jservice.io/api/random?count=1'
#
# response = requests.get(f"{BASE_URL}")
#
#
# def pars(response):
#     a = response.json()
#     w = {}
#     for i in a:
#         w = i
#     return w
#print(pars(response)['id'])