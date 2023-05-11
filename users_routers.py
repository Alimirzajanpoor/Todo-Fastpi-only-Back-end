from fastapi import APIRouter,Depends,HTTPException,status
import database,schemas,models,hashing
import database,oaut2,schemas
from sqlalchemy.orm import Session
from typing import List
import users_repository


router=APIRouter(
    prefix="/user",
    tags=['users']
)
get_db=database.get_db

@router.post('/')
def create_user(request:schemas.User,db: Session= Depends(get_db)):
    return users_repository.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session= Depends(get_db)):
    return users_repository.show(id,db)
@router.get("/")
async def read_users_me(current_user: schemas.User = Depends(oaut2.get_current_user)):
    return current_user