from sqlalchemy import Boolean, Column, String, Text, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from database.base import Base
from time import time


import uuid

class RiotUser(Base):
    __tablename__ = "riotuser"
    riotuid = Column(String(16), nullable=False, primary_key=True)
    nickname= Column(String(16), nullable=False)

class RegisteredUsers(Base):
    __tablename__= 'regiseredusers'

    inherenceid = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(20),nullable=False)
    password = Column(String(16),nullable=False)
    email_val = Column(Boolean, default=False)


class RegisterToken(Base):
    __tablename__ = 'registertoken'

    email=Column(String(20), primary_key=True)
    token=Column(String(120))