from typing import List
from fastapi import APIRouter,Depends
import schemas,database,models,hashing,oaut2
from fastapi import FastAPI,Depends,status,Response
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import blog_repository
router=APIRouter(
    prefix="/blog",
    tags=['blogs']
)
get_db=database.get_db
@router.get('/showall/')
def all(db: Session= Depends(database.get_db),current_user: schemas.User= Depends(oaut2.get_current_user)):
    if  not blog_repository.get_all(db):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='NO DATA IN DB')
    
    return blog_repository.get_all(db)

@router.post('/createblog/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,db: Session = Depends(get_db),current_user: schemas.User= Depends(oaut2.get_current_user)):
    return blog_repository.create(request,db,current_user['id'])



@router.delete('/delete_user={id}/',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int,db:Session=Depends(get_db),current_user: schemas.User= Depends(oaut2.get_current_user)):
    return blog_repository.destroy(id,db)

@router.put('/update_user={id}/',status_code=status.HTTP_202_ACCEPTED)
def update(id: int,request: schemas.Blog,db: Session= Depends(get_db),current_user: schemas.User= Depends(oaut2.get_current_user)):
    return blog_repository.update(id,request,db)
@router.get('/show_user={id}/',status_code=200,response_model=schemas.Showblog)
def show(id: int,db: Session= Depends(get_db),current_user: schemas.User= Depends(oaut2.get_current_user)):
    return blog_repository.show(id,db)


