#!/usr/bin/python3
"""Module for Filestore class."""
import datetime
import json
import os


class FileStorage:

    """ Class Acts as a database to Json files """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionaries from private objects """
        return FileStorage.__objects

    def new(self, obj):
        """ save name and id of the object """
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Give Each Object a Serial Number in Json file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, file)

    def classes(self):
        """ Retrive classes and their values and atteributes """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "review": Review}
        return classes

    def reload(self):
        """Reload Stored Data into Json file """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Return Atteributes for each Class"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
