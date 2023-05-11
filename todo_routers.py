from fastapi import APIRouter,Depends,HTTPException,status
import database,schemas,models,hashing
import database
from sqlalchemy.orm import Session
from typing import List
from tasks import app
from datetime import datetime
from todo_repository import todo_apply,delete_task
import oaut2
import uuid
router=APIRouter(
    prefix="/todo",
    tags=['todo']
)


@router.post('/create_task')
async def create_todo(request:schemas.todo_data, telegram_id : str,current_user: schemas.User = Depends(oaut2.get_current_user)):
    todo_id=t = current_user["sub"]
    schemas.todo_data.task_id=todo_id
    await todo_apply(request.title,request.detail,request.remind_on,telegram_id,todo_id)
    
    return {"your task_id": todo_id,"user": current_user }
@router.post('/remove_task')
async def remove_todo(current_user: schemas.User = Depends(oaut2.get_current_user)):
    await delete_task(current_user["sub"])
    
    return {"user": current_user,"status":"your task is removed" }
    