#!/usr/bin/python3
"""Defines a class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a Review object"""
    place_id = ""
    user_id = ""
    text = ""
