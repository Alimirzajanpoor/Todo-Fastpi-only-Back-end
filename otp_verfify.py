from sqlalchemy.orm import Session
import models,schemas,sendmsg
from fastapi import HTTPException,status

import random
def generate_otp():
    global rdm
    rdm=random.randint(1000,5000)
    return rdm
def verify_otp(otp:int,db: Session,userid: int):
    body=db.query(models.Otp).filter(models.Otp.user_id==userid)

    if body.first()==None:
        try:
            if otp==rdm:

                Verified=models.Otp(telegram_otp='Verified',user_id=userid)
                db.add(Verified)
                db.commit()
                db.refresh(Verified)
                raise HTTPException(detail="Verified",status_code=status.HTTP_200_OK)
              
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Wrong otp")

        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Wrong otp")
        
    for i in body:
        if i.__dict__['telegram_otp']=='Verified':
            return 'already verified'




