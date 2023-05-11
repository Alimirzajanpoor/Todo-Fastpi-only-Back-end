from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import models
import schemas,database,hashing,tokenbis

from sqlalchemy.orm import Session

router=APIRouter(
    tags=['authentication']
)
@router.post('/login')
def login(request:OAuth2PasswordRequestForm= Depends(),db:Session= Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email== request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")

    if not hashing.Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='incorrect password')

   
    access_token = tokenbis.create_access_token(data={"sub": user.email,'id':user.id})
    return {"access_token": access_token, "token_type": "bearer"}