#!/usr/bin/python3
"""base model class"""
import uuid
import datetime
import models


class BaseModel:
    """basemodel class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for ky, vl in kwargs.items():
                if ky != '__class__':
                    setattr(self, ky, vl)
                    if ky in ('created_at', 'updated_at'):
                        setattr(self, ky, datetime.datetime.
                                strptime(vl, '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """sets to tring format"""
        cname = self.__class__.__name__
        str = "[{}]".format(cname)
        str += "({})".format(self.id)
        str += "{}".format(self.__dict__)
        return str

    def save(self):
        """saves time object was created"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary func"""
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return mydict
