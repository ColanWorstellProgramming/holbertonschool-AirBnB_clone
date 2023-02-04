#!/usr/bin/python3
"""base model class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """basemodel class"""
    def __init__(self, id=0, created_at=0, updated_at=0):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """sets to tring format"""
        strect = "[{}]".format(self.__class__.__name__)
        strect += "({})".format(self.id)
        strect += "{}".format(self.__dict__)
        return strect

    def save(self):
        """saves time object was created"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """dictionary func"""
        mydict = self.__dict__
        mydict["__class__"] = self.__class__
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return mydict
