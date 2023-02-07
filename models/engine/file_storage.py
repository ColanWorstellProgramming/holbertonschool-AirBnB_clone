#!/usr/bin/python3
"""storage class"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City


class FileStorage:
    """file storage"""
    __objects = {}
    __file_path = 'file.json'

    def all(self):
        """returns all objects in dict"""
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            moby = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(moby, f)

    def reload(self):
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                moby = json.load(f.read())
                for key, value in moby.items():
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
