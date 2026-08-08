#!/usr/bin/python3
"""Module that multiplies two matrices using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy.dot.

    Args:
        m_a: first matrix.
        m_b: second matrix.

    Returns:
        numpy.ndarray: the product matrix.
    """
    return np.dot(m_a, m_b)
