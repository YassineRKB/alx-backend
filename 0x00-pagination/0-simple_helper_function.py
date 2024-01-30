#!/usr/bin/env python3
"""module for task 0"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    start = page_size * (page - 1)
    end = page * page_size
    res = (start, end)
    return res
