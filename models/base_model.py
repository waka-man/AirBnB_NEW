"""
BaseModel
"""
import uuid
import datetime
from models import storage


class BaseModel:
    """
    Base class for all other classes
    """
    def __init__(self, **kwargs):
        """
        Initialize a BaseModel instance.
        If no keyword arguments are given,
        instance attributes are set to default
        values. Otherwise, the instance
        is populated with the given keyword
        arguments.
        Default values are:
        - id: a uuid4
        - created_at: the current datetime
        - updated_at: the current datetime
        If the keyword arguments contain a
        "created_at" or "updated_at" key,
        the value is converted to a datetime object.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the instance.

        The returned string includes the class name, the instance's unique ID,
        and a dictionary of the instance's attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute of
        the instance with the current datetime.
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance.
        The returned dictionary includes all
        the attributes of the instance and
        a "__class__" key with the class name
        of the instance. DateTime attributes
        are converted to ISO 8601 format strings.
        Args:
            None
        Returns:
            dict: a dictionary representation of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        for key, value in new_dict.items():
            if isinstance(value, datetime.datetime):
                new_dict[key] = value.isoformat()
        return new_dict
