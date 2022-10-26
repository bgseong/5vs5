from sqlalchemy import Boolean, Column, String, Text, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from database.base import Base
from .userDB import RiotUser
import uuid
from sqlalchemy.orm import relationship, backref


class Game(Base):
    __tablename__= 'games'

    id=Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_ids = Column(String(120), ForeignKey(RiotUser.riotuid), nullable=True)
    ids_user=relationship('RiotUser', foreign_keys=[user_ids], backref=backref('game_by_user',uselist=False))
    champion=Column(String(20), nullable=False)
    kill=Column(String(20), nullable=False)
    death=Column(String(20), nullable=False)
    assist=Column(String(20), nullable=False)
