from datetime import datetime

from pydantic import BaseModel

class Ques(BaseModel):
    id: int
    question:str
    answer:str
    created_at:datetime