#!/usr/bin/python3
"""storage class"""
import json
from os import path

class FileStorage:
    """file storage"""
    __objects = {}
    __file_path = 'objects.json'

    def all(self):
        """returns all objects in dict"""
        return self.__objects

    def new(self, obj):
       key = obj.__class__.__name__ + "." + obj.id
       self.__objects[key] = obj

    def save(self):
        jsondict = {}
        jsondict = self.__objects
        with open( "__file_path" , "w") as f:
            json.dump(jsondict, f)

    def reload(self):
        if self.__file_path:
            try: self.__objects = json.loads(self.__objects)
            except: not self.__file_path                
