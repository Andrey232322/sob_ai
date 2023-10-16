from sqlalchemy import Column,String,Integer,Boolean,DATETIME
from db import Base

class Ques(Base):
    __tablename__ = 'Ques'

    id = Column(Integer,primary_key=True)
    question = Column(String, unique=True)
    answer = Column(String)
    created_at = Column(DATETIME)