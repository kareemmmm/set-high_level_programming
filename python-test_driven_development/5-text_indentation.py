#!/usr/bin/python3
"""Module that prints text with indentation"""


def text_indentation(text):
    """Prints text with 2 new lines after each ., ? and : character.

    Args:
        text: the string to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip())
