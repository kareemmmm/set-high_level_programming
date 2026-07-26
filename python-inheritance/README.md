# Python - Inheritance

## Description
This project covers the core principles of Object-Oriented Programming (OOP) in Python with a focus on **Inheritance**, **Subclasses**, **Method Overriding**, **Abstract/Base Classes**, and **Custom Exceptions**.

## Concepts Covered
- What is inheritance and how to create a subclass in Python.
- Understanding `isinstance()`, `issubclass()`, `type()`, and `dir()`.
- Method overriding and calling base class constructors via `super()`.
- Class attribute validation and handling custom exception raising.
- Inverting operator behavior using special magic methods (`__eq__`, `__ne__`).
- Dynamically setting object attributes using `setattr()` and checking `__dict__`.

## Files Summary

| File | Description |
| --- | --- |
| `0-lookup.py` | Function returning the list of available attributes and methods of an object |
| `1-my_list.py` | Class `MyList` inheriting from `list` with a `print_sorted()` method |
| `tests/1-my_list.txt` | Doctest suite for `1-my_list.py` |
| `2-is_same_class.py` | Function checking if an object is exactly an instance of a specified class |
| `3-is_kind_of_class.py` | Function checking if an object is an instance of, or inherited from, a class |
| `4-inherits_from.py` | Function checking if an object is a subclass instance (excluding exact class match) |
| `5-base_geometry.py` | Empty class `BaseGeometry` |
| `6-base_geometry.py` | Class `BaseGeometry` with unimplemented `area()` method |
| `7-base_geometry.py` | Class `BaseGeometry` with `integer_validator()` method |
| `tests/7-base_geometry.txt` | Doctest suite for `7-base_geometry.py` |
| `8-rectangle.py` | Class `Rectangle` inheriting from `BaseGeometry` with validated dimensions |
| `9-rectangle.py` | Class `Rectangle` with implemented `area()` and `__str__()` representation |
| `10-square.py` | Class `Square` inheriting from `Rectangle` |
| `11-square.py` | Class `Square` with custom `__str__()` representation |
| `100-my_int.py` | Class `MyInt` inheriting from `int` with inverted `==` and `!=` operators |
| `101-add_attribute.py` | Function adding new attributes to objects if supported |
