# Python - More Classes and Objects

This directory contains projects focused on Object-Oriented Programming (OOP) concepts in Python, specifically covering advanced class features, encapsulation, properties (getters & setters), special methods (`__str__`, `__repr__`, `__del__`), class/static attributes and methods, as well as a practical application using backtracking to solve the classic N-Queens puzzle.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Tasks & Project Files](#tasks--project-files)
  - [0. Simple Rectangle](#0-simple-rectangle)
  - [1. Real Definition of a Rectangle](#1-real-definition-of-a-rectangle)
  - [2. Area and Perimeter](#2-area-and-perimeter)
  - [3. String Representation](#3-string-representation)
  - [4. Eval is Magic](#4-eval-is-magic)
  - [5. Detect Instance Deletion](#5-detect-instance-deletion)
  - [6. How Many Instances](#6-how-many-instances)
  - [7. Change Representation](#7-change-representation)
  - [8. Compare Rectangles](#8-compare-rectangles)
  - [9. A Square is a Rectangle](#9-a-square-is-a-rectangle)
  - [10. N Queens](#10-n-queens)
- [Usage & Testing](#usage--testing)
- [Repository Structure](#repository-structure)

---

## 🛠️ Overview

- **Repository:** `set-high_level_programming`
- **Directory:** `python-more_classes`
- **Language:** Python 3 (PEP 8 standard compliance)

---

## 📋 Requirements

- Environment: Written for **Python 3.x**.
- Code Style: Complies with `pycodestyle` (version 2.8.*).
- Execution: All `.py` files are executable (`chmod +x <filename>.py`).
- Constraints: No external modules imported (except `sys` for Task 10).

---

## 📁 Tasks & Project Files

### 0. Simple Rectangle
- **File:** `0-rectangle.py`
- **Description:** Defines an empty class `Rectangle`.

---

### 1. Real Definition of a Rectangle
- **File:** `1-rectangle.py`
- **Description:** Defines a class `Rectangle` with private instance attributes `width` and `height`, controlled using getters and setters (`@property`).
- **Validation:** Raises `TypeError` if dimensions are not integers, and `ValueError` if less than `0`.

---

### 2. Area and Perimeter
- **File:** `2-rectangle.py`
- **Description:** Adds public instance methods `area(self)` and `perimeter(self)` to calculate the dimensions. Returns `0` for perimeter if either dimension is `0`.

---

### 3. String Representation
- **File:** `3-rectangle.py`
- **Description:** Overrides `__str__` to print the rectangle using the `#` character. Returns an empty string if `width` or `height` is `0`.

---

### 4. Eval is Magic
- **File:** `4-rectangle.py`
- **Description:** Overrides `__repr__` to return a string representation that allows recreating a new instance using `eval()`.

---

### 5. Detect Instance Deletion
- **File:** `5-rectangle.py`
- **Description:** Overrides `__del__` to output the message `"Bye rectangle..."` when an instance of `Rectangle` is deleted.

---

### 6. How Many Instances
- **File:** `6-rectangle.py`
- **Description:** Introduces a public class attribute `number_of_instances` that tracks active instances (incremented on initialization, decremented on deletion).

---

### 7. Change Representation
- **File:** `7-rectangle.py`
- **Description:** Adds a public class attribute `print_symbol` (initialized to `#`) used to customize the character representation of the rectangle.

---

### 8. Compare Rectangles
- **File:** `8-rectangle.py`
- **Description:** Adds a static method `bigger_or_equal(rect_1, rect_2)` that returns the largest rectangle based on area.

---

### 9. A Square is a Rectangle
- **File:** `9-rectangle.py`
- **Description:** Adds a class method `square(cls, size=0)` that creates a new `Rectangle` instance with `width == height == size`.

---

### 10. N Queens
- **File:** `101-nqueens.py`
- **Description:** A standalone Python program that solves the classic **N Queens puzzle** (placing $N$ non-attacking queens on an $N \times N$ chessboard) using a backtracking algorithm.
- **Usage:** `./101-nqueens.py N`

---

## 🚀 Usage & Testing

### Running Rectangle Tasks
Create a main script (e.g., `1-main.py`) and test the imported class:

```bash
./1-main.py
