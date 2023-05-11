from fastapi import FastAPI
import schemas,models,database
from database import engine,SessionLocal
import blog_routers,users_routers,authentication_routers,otp_routers,todo_routers
app=FastAPI()
models.Base.metadata.create_all(engine)
get_db=database.get_db
app.include_router(authentication_routers.router)
app.include_router(blog_routers.router)
app.include_router(users_routers.router)
app.include_router(otp_routers.router)
app.include_router(todo_routers.router)
