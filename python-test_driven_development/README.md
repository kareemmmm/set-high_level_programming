# Python - Test-Driven Development

This project focuses on the implementation of **Test-Driven Development (TDD)** practices in Python. The goal is to write clean, fully validated, and error-proof code while ensuring high testing coverage using both `doctest` and `unittest` modules.

## Technologies
* **Language:** Python 3.8.5
* **Style Guide:** Pycodestyle (version 2.8.*)
* **Testing Modules:** `doctest` and `unittest`
* **OS Environment:** Ubuntu 20.04 LTS

## General Requirements
* Allowed editors: `vi`, `vim`, `emacs`.
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
* All your files should end with a new line.
* The first line of all your files should be exactly `#!/usr/bin/python3`.
* A `README.md` file, at the root of the folder of the project, is mandatory.
* Your code should use the `pycodestyle` style (version 2.8.*).
* All your files must be executable.
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
* All your test files should be inside a folder named `tests`.
* All your test files should be text files (extension: `.txt`) for `doctest`.
* All your tests should be executed by running: `python3 -m doctest ./tests/*`.

---

## Tasks Summary

| Task | File(s) | Description | Test File |
| --- | --- | --- | --- |
| **0. Integers Addition** | `0-add_integer.py` | Function that adds 2 integers or floats casted to integers. | `tests/0-add_integer.txt` |
| **1. Divide a Matrix** | `2-matrix_divided.py` | Function that divides all elements of a matrix by a given divisor. | `tests/2-matrix_divided.txt` |
| **2. Say my Name** | `3-say_my_name.py` | Function that prints `My name is <first name> <last name>`. | `tests/3-say_my_name.txt` |
| **3. Print Square** | `4-print_square.py` | Function that prints a square with the `#` character based on size. | `tests/4-print_square.txt` |
| **4. Text Indentation** | `5-text_indentation.py` | Prints a text with 2 new lines after each of these characters: `.`, `?` and `:`. | `tests/5-text_indentation.txt` |
| **5. Max Integer - Unittest** | `tests/6-max_integer_test.py` | Unittests for an existing `max_integer(list=[])` function. | *Self-contained unittest* |
| **6. Matrix Multiplication** | `100-matrix_mul.py` | Function that multiplies 2 matrices after thorough custom validations. | `tests/100-matrix_mul.txt` |
| **7. Lazy Matrix Multiplication**| `101-lazy_matrix_mul.py` | Multiplies 2 matrices by using the `NumPy` module interface. | `tests/101-lazy_matrix_mul.txt` |

---

## Testing Examples

### Running Doctests
To run tests for a specific task using the `doctest` module interactive mode:
```bash
python3 -m doctest -v ./tests/0-add_integer.txt
