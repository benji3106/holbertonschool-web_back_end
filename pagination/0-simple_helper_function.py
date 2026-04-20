#!/usr/bin/env python3

"""
module with a function page 1
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    the function returns the first and last indexes of the page
    depends on the size of the page
    """
    result: Tuple = ((page - 1) * page_size, page * page_size)
    return result
