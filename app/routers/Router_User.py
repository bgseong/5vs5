from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import schema
from database import base
from database.models import userDB
from database.models import gameDB
from database.models import civillDB

from typing import Optional, List

router=APIRouter(
    prefix="/civill"
)

@router.get('/getGame', response_model=List[schema.ResponseGame])
async def get_games(db: Session = Depends(base.get_db)):
    games = db.query(gameDB.Game).all()
    return games

@router.get('/getUser', response_model=List[schema.ResponseUser])
async def get_users(db: Session = Depends(base.get_db)):
    users = db.query(userDB.RegisteredUsers).all()
    return users

@router.post('/postuser', response_model=schema.ResponseUser)
async def register_user(req: schema.RequestUser, db: Session = Depends(base.get_db)):
    user = userDB.RegisteredUsers(**req.dict())
    db.add(user)
    db.commit()

    return user

