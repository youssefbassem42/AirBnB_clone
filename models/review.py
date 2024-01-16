#!/usr/bin/python3
""" This File for RateUs The Class Objects """
from models.base_model import BaseModel


class Review(BaseModel):
    """ RateUs Class """

    place_id = ""
    user_id = ""
    text = ""
