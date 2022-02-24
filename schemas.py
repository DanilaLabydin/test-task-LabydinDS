from typing import List,Optional
from pydantic import BaseModel, validator
from fastapi import Query


class Postin(BaseModel):
    request: str

    class Config:
        orm_mode = True

    @validator('request')
    def check_acceptable_values(cls, v):
        accept_values = ['0', '1', '2', '3', '4',
                         '5', '6', '7', '8', '9',
                         '.', '+', '-', '*', '/',
                         '(', ')']
        for i in v.strip():
            if i != ' ' and i not in accept_values:
                raise ValueError('You wrote the unacceptable value/s')
        return v


class Post(BaseModel):
    id: int
    request: str
