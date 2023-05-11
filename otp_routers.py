from typing import List
from fastapi import APIRouter,Depends
import schemas,database,models,hashing,oaut2,otp_verfify
from fastapi import FastAPI,Depends,status,Response
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session


router=APIRouter(
    prefix="/otp",
    tags=['otps'],
)

get_db=database.get_db
@router.get('/')
def generate_otp(db: Session= Depends(database.get_db),current_user: schemas.User= Depends(oaut2.get_current_user)):
    return otp_verfify.generate_otp()
@router.post('/',status_code=status.HTTP_201_CREATED)
def verify(otp:int,db: Session= Depends(database.get_db), current_user: schemas.User= Depends(oaut2.get_current_user)):

    return otp_verfify.verify_otp(otp,db,current_user['id'])
    