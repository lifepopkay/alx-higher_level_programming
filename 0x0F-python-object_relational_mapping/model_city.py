#!/usr/bin/python3

"""
    City class
"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, nullable=False,
                      Foreignkey('states.id'))
