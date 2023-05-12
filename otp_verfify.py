from sqlalchemy.orm import Session
import models,schemas,sendmsg
from sendmsg import send_text
from fastapi import HTTPException,status

import random
def generate_otp(telegram_id):
    global rdm
    rdm=random.randint(1000,5000)
    send_text(telegram_id,"Generated OTP"+str(rdm))
    return rdm

def verify_otp(otp:int,db: Session,userid: int):
    body=db.query(models.Otp).filter(models.Otp.user_id==userid)
    if body.first()==None:

        try:
            if otp == rdm:
                Verified = models.Otp(telegram_otp='Verified', user_id=userid)
                db.add(Verified)
                db.commit()
                db.refresh(Verified)
                raise HTTPException(status_code=status.HTTP_200_OK, detail="OTP verified")
        except NameError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OTP not generated yet")
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wrong OTP")
        

    
        
    for i in body:
        if i.__dict__['telegram_otp']=='Verified':
            return 'already verified'




