#!/usr/bin/python3
"""This class inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class that inherits from BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
