#!/usr/bin/python3
"""
This module contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """Creates State table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")