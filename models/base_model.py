#!/usr/bin/python3
"""base model class"""
from uuid import uuid4
from datetime import datetime
time = '%Y-%m-%dT%H:%M:%S.%f'
class BaseModel:
    """basemodel class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'upated_at':
                    value.isoformat == datetime.utcnow()
                if key != __class__:
                    setattr(self, key, value)
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.datetime.strptime(value, time))

        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """sets to tring format"""
        str = "[{}]".format(self.__class__.__name__)
        str += "({})".format(self.id)
        str += "{}".format(self.__dict__)
        return str

    def save(self):
        """saves time object was created"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """dictionary func"""
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return mydict
