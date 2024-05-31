#!/usr/bin/python3

"""
    City class
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, 
                nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, nullable=False,
                      ForeignKey("states.id"))
