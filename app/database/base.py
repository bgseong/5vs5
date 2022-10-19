from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:2898@localhost:5432/memo')
db_session=scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base=declarative_base()

from database.models.civillDB import *
from database.models.gameDB import *
from database.models.userDB import *

Base.metadata.create_all(bind=engine)

def get_db():
    db=None
    try:
        db= db_session()
        yield db
    finally:
        db.close()