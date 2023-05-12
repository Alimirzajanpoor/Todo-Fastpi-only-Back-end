from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Union,Optional
from datetime import datetime

class BlogBase(BaseModel):
    title:str
    body: str
class Blog(BlogBase):
    title:str
    body: str
    class Config():
        orm_mode=True
class User(BaseModel):
    name:str
    email:str
    password:str
class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog]=[]
    class Config():
        orm_mode=True
class Showblog(BaseModel):
    title:str
    body: str
    creator: ShowUser
    class Config():
        orm_mode=True

class Login(BaseModel):
    username: str
    password: str
class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    username: Union[str, None] = None
class todo_data(BaseModel):
    title: str
    detail: Optional[str] = None
    is_done: bool = False
    remind_on: str = datetime.now().strftime("%m/%d/%y %H:%M:%S")
    task_id: str =None
