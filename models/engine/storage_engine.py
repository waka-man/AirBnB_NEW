"""
FileStorage class
"""
import os
import json


class FileStorage():
    """
    FileStorage class
    """
    def __init__(self):
        self.__filepath = "file.json"
        self.__objects = {}

    def all(self):
        """
        all(self): returns a dictionary of all
        objects by <class name>.<id>
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the storage dictionary.

        Args:
            obj: The object to add to the storage.
            The key is generated using
            the object's class name and id,
            in the format <class name>.<id>.
        """

        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        save(self): serializes __objects to
        the JSON file (path: __file_path)
        """
        with open(self.__filepath, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)

        """
        if os.path.exists(self.__filepath):
            try:
                with open(self.__filepath, "r", encoding="utf-8") as f:
                    from models.base_model import BaseModel
                    for key, value in json.load(f).items():
                        self.__objects[key] = BaseModel(**value)
            except FileNotFoundError:
                pass
