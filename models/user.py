#!/usr/bin/python3
from models.base_model import BaseModel
"""This class inherits from BaseModel"""


class User(BaseModel):
    """A class that inherits from BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
