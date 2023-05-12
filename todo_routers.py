from fastapi import APIRouter,Depends
import database,schemas,models
import database

from typing import List
from tasks import app
from datetime import datetime
from todo_repository import todo_apply,delete_task
import oaut2
from sqlalchemy.orm import Session
router=APIRouter(
    prefix="/todo",
    tags=['todo']
)
def convert_date_string(date_string):
    
    date_obj = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S')
    return date_obj
async def Verify_todo(user_id,db):
    body=db.query(models.Otp).filter(models.Otp.user_id==user_id)
    if body.first()==None:
        return 0    
    tele_status = db.query(models.Otp.telegram_otm).filter(models.Otp.user_id == user_id).first()
    if tele_status=="Verified":
            return 1
@router.post('/create_task')
async def create_todo(request:schemas.todo_data, telegram_id : str,current_user: schemas.User = Depends(oaut2.get_current_user),db: Session= Depends(database.get_db)):
    todo_id=current_user["sub"]
    
    if Verify_todo(current_user["id"],db)==1:
        schemas.todo_data.task_id=todo_id

        await todo_apply(request.title,request.detail,convert_date_string(request.remind_on),telegram_id,todo_id,current_user["id"],db)
    
    return {"your task_id": todo_id,"user": current_user }
@router.post('/remove_task')
async def remove_todo(db: Session= Depends(database.get_db),current_user: schemas.User = Depends(oaut2.get_current_user)):
    await delete_task(current_user["sub"],current_user["id"],db)
    
    return {"user": current_user,"status":"your task is removed" }
    
