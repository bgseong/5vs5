from pydantic import BaseModel
from typing import Optional

class RequestUser(BaseModel):
    name : str

class ResponseUser(BaseModel):
    inherenceid : str
    name : str

    class Config:
        orm_mode = True

class RequestGame(BaseModel):
    champion: str
    kill: str
    death: str
    assist: str

class ResponseGame(BaseModel):
    id : str
    user: str
    champion: str
    kill: str
    death: str
    assist: str

    class Config:
        orm_mode = True

class RequestReg(BaseModel):
    nickname : str
    name : str
    password : str

class ResponseReg(RequestReg):
    id: str

    class Config:
        orm_mode = True


class RequestCivill(BaseModel):
    TotalKill: str
    TotalDeath: str
    TotalAssist: str


class ResponseCivill(RequestCivill):
    id: str
    team_ids : Optional[str]

    class Config:
        orm_mode = True

class Register(BaseModel):
    email: Optional[str]
    password: Optional[str]