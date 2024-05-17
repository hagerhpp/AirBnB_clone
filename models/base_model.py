#!/usr/bin/python3
"""
module to define the "baseClass"
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    define all common methods and attributes of the classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        updates updated_at attribute with the current datetime that changed at
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns dictionary containing content (key: values) of __dict__
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict

    def __str__(self):
        """
        return string format that contain class name, class id and class dict
        """
        class_name = self.__class__.__name__
        ret = "({}) ({}) {}".format(class_name, self.id, self.__dict__)
        return ret
