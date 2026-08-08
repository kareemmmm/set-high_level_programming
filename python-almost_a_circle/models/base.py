#!/usr/bin/python3
"""Defines the Base class for all other classes in the project."""
import json
import csv
import os


class Base:
    """Represent the base model for managing id attribute."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation."""
        if json_string is None or json_string == "" or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a list of objects to a CSV file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from a CSV file."""
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []
        instances = []
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                row = [int(val) for val in row]
                if cls.__name__ == "Rectangle":
                    d = {"id": row[0], "width": row[1], "height": row[2], "x": row[3], "y": row[4]}
                elif cls.__name__ == "Square":
                    d = {"id": row[0], "size": row[1], "x": row[2], "y": row[3]}
                instances.append(cls.create(**d))
        return instances
