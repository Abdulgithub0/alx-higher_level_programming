#!/usr/bin/python3

"""
Defining class State that mapped to table states in hbtn_0e_6_usa db
"""

from sys import argv
from sqlalchemy import Column, Table, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ht = argv[1]
pw = argv[2]
db = argv[3]

# Configuring communication channel info
engine = create_engine(f"mysql+mysqldb://{ht}:{pw}@localhost/{db}",
                       pool_pre_ping=True)

# Establishing communication channel to argv[3] db of mysql process(3306)
Session = sessionmaker(bind=engine)
session = Session()

# construct declarative_base class
Base = declarative_base()


class State(Base):
    """State Class that inherits from Base"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


# Base.metadata.create_all(engine)
