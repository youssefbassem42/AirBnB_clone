#!/usr/bin/python3
""" This File for User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class User For User info """

    email = ""
    password = ""
    FirstName = ""
    LastName = ""
