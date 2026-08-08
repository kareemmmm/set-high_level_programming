#!/usr/bin/python3
"""Module for matrix multiplication validations."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a: Matrix A (list of lists of ints/floats).
        m_b: Matrix B (list of lists of ints/floats).

    Returns:
        The resulting multiplied matrix.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
        
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
        
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
        
    for row in m_a:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("m_b should contain only integers or floats")
            
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
        
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
        
    res = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]
    return res
