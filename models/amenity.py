#!/usr/bin/python3
"""This is  Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv


class Amenity(BaseModel, Base):
    """This is amenity class"""
    __tablename__ = 'amenities'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
