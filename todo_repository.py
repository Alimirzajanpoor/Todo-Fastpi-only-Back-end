from datetime import datetime
from tasks import run_test,deschedule_todo

async def todo_apply(title: str,detail : str, date : datetime,telegram_id : str,todo_id: str):
    
    await run_test(title,detail,date,telegram_id,todo_id)
async def delete_task(todo_id: str):
    
    await deschedule_todo(todo_id)
