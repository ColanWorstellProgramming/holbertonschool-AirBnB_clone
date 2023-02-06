#!/usr/bin/python3
"""storage class"""
import json
import os

class FileStorage:
    """file storage"""
    __objects = {}
    __file_path = 'file.json'

    def all(self):
        """returns all objects in dict"""
        return self.__objects

    def new(self, obj):
       key = obj.__class__.__name__ + "." + obj.id
       self.__objects[key] = obj

    def save(self):
        obdict = {}
        for key, value in self.__objects.items():
            obdict[key] = value.to_dict()
        with open( "__file_path" , "w", encoding="utf-8") as f:
            (json.dump(obdict, f))

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                LoadDict = json.loads(f.read())
            for key, val in LoadDict.items():
                self.__objects[key] = eval(val["__class__"])(**val)