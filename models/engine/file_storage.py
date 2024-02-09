#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
"""Defines a file storage class that serializes instances to a JSON file
and deserializes a JSON file to instances"""


class FileStorage:
    """class for serialization and deserialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """adds new object to the __objects dictionary
        Args:
            obj: object to be added
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes instances to a JSON file"""
        objects_dict = {}
        for key, value in FileStorage.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """deserializes a JSON file to instances"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                objects_dict = json.load(f)
            for key, value in objects_dict.items():
                cls = value["__class__"]
                del value["__class__"]
                FileStorage.__objects[key] = eval(cls)(**value)

        except FileNotFoundError:
            pass
