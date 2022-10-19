from sqlalchemy import Boolean, Column, String, Text, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from database.base import Base
from .userDB import RiotUser
import uuid


class Game(Base):
    __tablename__= 'games'

    id=Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    user=Column(String(120), ForeignKey(RiotUser.riotuid))
    champion=Column(String(20), nullable=False)
    kill=Column(String(20), nullable=False)
    death=Column(String(20), nullable=False)
    assist=Column(String(20), nullable=False)
