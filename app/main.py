import os
import bcrypt
import uvicorn
from fastapi import FastAPI, Response, Depends, UploadFile, File
from database import schema
from starlette.responses import JSONResponse
from typing import Optional, List
from sqlalchemy.orm import Session
from database import base
from database.models import userDB
from database.models import gameDB
from database.models import civillDB

from starlette.middleware.cors import CORSMiddleware
import json

import uuid


app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/getReg', response_model=List[schema.ResponseReg])
async def get_memos(db: Session = Depends(base.get_db)):
    users = db.query(userDB.User).all()
    return users


@app.get('/getGame', response_model=List[schema.ResponseGame])
async def get_games(db: Session = Depends(base.get_db)):
    games = db.query(gameDB.Game).all()
    return games

@app.get('/getUser', response_model=List[schema.ResponseUser])
async def get_users(db: Session = Depends(base.get_db)):
    users = db.query(userDB.RegisteredUsers).all()
    return users

@app.post('/postuser', response_model=schema.ResponseUser)
async def register_user(req: schema.RequestUser, db: Session = Depends(base.get_db)):
    user = userDB.RegisteredUsers(**req.dict())
    db.add(user)
    db.commit()

    return user

@app.post('/upload')
async def uploadFile(file:UploadFile, db: Session = Depends(base.get_db)):
    content = await file.read()
    with open(file.filename,'wb') as f:
        f.write(content)
    with open(file.filename, "r", encoding="utf8", errors="ignore") as f:
        a = f.readlines()[3]
        js = json.loads(f"{{{'{'.join(a.split('{')[1:-1])}{{{'}'.join(a.split('{')[-1].split('}')[:2])}}}")
        js['statsJson'] = json.loads(js['statsJson'])
        TotalScore={"CHAMPIONS_KILLED" :0, "NUM_DEATHS":0, "ASSISTS":0}
        for j in js['statsJson']:
            TotalScore["CHAMPIONS_KILLED"] += int(j["CHAMPIONS_KILLED"])
            TotalScore["NUM_DEATHS"] += int(j["NUM_DEATHS"])
            TotalScore["ASSISTS"] += int(j["ASSISTS"])
    db.add(civillDB.Civill(TotalKill=str(TotalScore["CHAMPIONS_KILLED"]), TotalDeath=str(TotalScore["NUM_DEATHS"]), TotalAssist=str(TotalScore["ASSISTS"])))
    db.commit()
    os.remove(file.filename)

    return {"filename":file.filename}

@app.get('/getcivill', response_model=List[schema.ResponseCivill])
async def get_civills(db: Session = Depends(base.get_db)):
    civills = db.query(civillDB.Civill).all()
    return civills

@app.post('/register')
async def register(req : schema.Register,db: Session = Depends(base.get_db)):
    req_dict = req.dict()
    check_user=db.query(userDB.RegisteredUsers).filter_by(email=req_dict['email']).count()
    if check_user:
        a=db.query(userDB.RegisteredUsers).filter_by(email=req_dict['email']).first()
        print(a.email_val)
        return "already"
    else:
        db.add(userDB.RegisteredUsers(email=req_dict['email'],password=req_dict['password']))
        Rtoken=str(uuid.uuid4()).replace("-","")
        db.add(userDB.RegisterToken(email=req_dict['email'], token=Rtoken))
        db.commit()

        import smtplib
        from email.mime.text import MIMEText

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('lol5vvss5@gmail.com', 'brnqrmocljvdcomq')
        msg = MIMEText('http://127.0.0.1:8000/oauth/token={}'.format(Rtoken))
        msg['Subject'] = '5vs5 이메일 인증'
        s.sendmail("lol5vvss5@gmail.com", req_dict['email'], msg.as_string())
        s.quit()
    return 0

@app.get('/oauth/token={token}')
async def oauth(token: str, db: Session = Depends(base.get_db)):
    check_token = db.query(userDB.RegisterToken).filter(userDB.RegisterToken.token == token).count()
    if check_token:
        email_info=db.query(userDB.RegisterToken).filter(userDB.RegisterToken.token == token).first()
        email=email_info.email
        db.delete(email_info)

        user_info=db.query(userDB.RegisteredUsers).filter(userDB.RegisteredUsers.email ==  email).first()
        user_info.email_val = True
        db.commit()
    else:
        return "no"
    return 0
