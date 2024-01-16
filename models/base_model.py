#!/usr/bin/python3
""" BaseModel for AirBnB Project """
import uuid
from datetime import datetime
from models import store
from models.engine.file_storage import FileStorage



class BaseModel:
    """ Base Class for All Classes """

    def __init__(self, *args, **kwargs):
        """ initial Constructor """
        if kwargs is not None and kwargs != {}:
            for k in kwargs.items():
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] == kwargs[k]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            store.new(self)


    def __str__(self):
        """ Return Format of the Class Representation """
        return f"[{type(self).__name__} ({self.id}) {self.__dict__}]"

    def save(self):
        """Save to Json file By File store Class"""
        self.updated_at = datetime.now()
        store.save()

    def to_dict(self):
        """ Converter from __dict__ to real dictionary """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary
