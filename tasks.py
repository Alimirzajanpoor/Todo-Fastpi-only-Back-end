from celery import Celery
from celery import shared_task,app
from celery.schedules import crontab
from datetime import datetime, timedelta
from sendmsg import send_text
from datetime import datetime

import os
from dotenv import load_dotenv
load_dotenv()

RABBITMQ_URL=os.getenv('RABBITMQ_URL')

app = Celery('tasks',backend='rpc://',broker=RABBITMQ_URL)


@app.task(bind=True)
def celery_schedule_todo(self, telegram_id: int, message: str):
    
    send_text(telegram_id, message)

async def schedule_todo(todo: dict, telegram_id: int,todo_id :str) -> None:
    message = f'<i>TODO reminder</i>\n\n<b>{todo.get("title")}</b>\n{todo.get("detail")}'
    
    celery_schedule_todo.apply_async(args=(telegram_id, message), eta=todo.get('remind_on'), task_id=todo_id)
async def deschedule_todo(todo_id: str) -> None:
    app.control.revoke(todo_id, terminated=True, signal='SIGKILL')

    
async def run_test(t,d,r,tele_id,todo_id):

    todo={"title":t,"detail":d,"remind_on":r}
    await schedule_todo(todo,tele_id,todo_id)

