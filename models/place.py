#!/usr/bin/python3
"""This file for Place Class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class for Place Objects """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    RoomsNumber = 0
    BathroomsNumber = 0
    MaxGuest = 0
    PriceByNight = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
