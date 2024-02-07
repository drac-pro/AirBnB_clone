#!/usr/bin/python3
import json
"""Defines a file storage class that serializes instances to a JSON file
and deserializes a JSON file to instances"""


class FileStorage:
    """class for serialization and deserialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """adds new object to the __objects dictionary
        Args:
            obj: object to be added
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes instances to a JSON file"""
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(objects_dict, f)

    def reload(self):
        """deserializes a JSON file to instances"""
        try:
            with open(self.__file_path, 'r') as f:
                objects_dict = json.load(f)

                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    module = __import__('models.base_model', fromlist=['BaseModel'])
                    cls = getattr(module, 'BaseModel')
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass


storage = FileStorage()
