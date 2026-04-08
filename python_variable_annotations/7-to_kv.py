#!/usr/bin/env python3
"""Module for creating a key-value tuple."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of a number as a float."""
    return (k, float(v ** 2))
