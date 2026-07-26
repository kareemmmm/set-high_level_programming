#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """Class MyList that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
