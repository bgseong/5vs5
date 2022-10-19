from sqlalchemy import Boolean, Column, String, Text, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from database.base import Base

from .userDB import RiotUser
import uuid

class Team(Base):
    __tablename__ = "teams"
    id = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    name=Column(String(20), nullable=False)
    user_ids = Column(String(120), ForeignKey(RiotUser.riotuid), nullable=True)
    ids_user=relationship('RiotUser', foreign_keys=[user_ids], backref=backref('team_by_user',uselist=False))
    TotalWin=Column(String(5),nullable=True)
    TotalLose=Column(String(5),nullable=True)
    TotalKill=Column(String(5),nullable=True)
    TotalDeath=Column(String(5),nullable=True)
    TotalAssist=Column(String(5),nullable=True)



class Civill(Base):
    __tablename__ = "civill"
    id= Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    team_ids = Column(String(120), ForeignKey(Team.id), nullable=True)
    ids_team = relationship('Team', foreign_keys=[team_ids], backref=backref('civill_by_team', uselist=False))
    TotalKill = Column(String(5), nullable=True)
    TotalDeath = Column(String(5), nullable=True)
    TotalAssist = Column(String(5), nullable=True)