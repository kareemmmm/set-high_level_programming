# Python - Everything is object

## Description
This project explores the fundamental concepts of Python's object model, including object identity, mutability vs immutability, reference passing vs value passing, and CPython internal optimizations such as integer caching and string interning.

## Concepts Covered
- **Objects and References:** Understanding `id()`, `type()`, `is`, and `==`.
- **Mutable Objects:** Lists, dictionaries, sets, and how in-place operations modify memory.
- **Immutable Objects:** Integers, floats, strings, tuples, and how modifications create new objects.
- **Argument Passing:** How Python uses "pass-by-object-reference".
- **CPython Internals:** Small integer caching (`NSMALLPOSINTS`, `NSMALLNEGINTS`), string interning, and optimizing instance attributes with `__slots__`.

## Files Summary

| File | Description |
| --- | --- |
| `0-answer.txt` | Function used to get the type of an object |
| `1-answer.txt` | Function used to get the identifier/memory address of an object |
| `2-answer.txt` | Evaluation of pointer references for distinct integer values |
| `3-answer.txt` | Evaluation of pointer references for identical small integer values |
| `4-answer.txt` | Evaluation of variable assignment referencing the same object |
| `5-answer.txt` | Evaluation of modified integer references |
| `6-answer.txt` | String equality comparison (`==`) |
| `7-answer.txt` | String identity comparison (`is`) |
| `8-answer.txt` | Literal string equality comparison |
| `9-answer.txt` | Literal string identity comparison |
| `10-answer.txt` | List value equality with distinct list objects |
| `11-answer.txt` | List object identity with distinct list objects |
| `12-answer.txt` | List value equality with assigned list reference |
| `13-answer.txt` | List object identity with assigned list reference |
| `14-answer.txt` | Output after in-place list mutation via `.append()` |
| `15-answer.txt` | Output after list concatenation assignment (`+`) |
| `16-answer.txt` | Demonstration of immutable integer parameter modification |
| `17-answer.txt` | Demonstration of mutable list parameter modification |
| `18-answer.txt` | Demonstration of reassigning function parameters |
| `19-copy_list.py` | Function that returns a copy of a list |
| `20-answer.txt` | Verification of an empty tuple `()` |
| `21-answer.txt` | Verification of a two-element tuple `(1, 2)` |
| `22-answer.txt` | Verification of single integer wrapped in parentheses `(1)` |
| `23-answer.txt` | Verification of a single-element tuple `(1, )` |
| `24-answer.txt` | Identity check on parenthesized single integers |
| `25-answer.txt` | Identity check on distinct tuple instances |
| `26-answer.txt` | Identity check on empty tuple singletons |
| `27-answer.txt` | Identity check after list concatenation assignment (`a = a + [...]`) |
| `28-answer.txt` | Identity check after in-place list extend (`a += [...]`) |
| `100-magic_string.py` | Function returning `"BestSchool"` repeated per call iteration |
| `101-locked_class.py` | Class restricting dynamic attributes except `first_name` using `__slots__` |
| `103-line1.txt`, `103-line2.txt` | CPython integer creation count for cached small integers |
| `104-line1.txt` to `104-line5.txt` | CPython integer creation and deletion behavior for large integers |
| `105-line1.txt` | Number of pre-allocated integer objects in CPython (`262`) |
| `106-line1.txt` to `106-line5.txt` | CPython string interning creation and deletion behavior |
