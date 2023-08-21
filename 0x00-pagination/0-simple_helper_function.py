#!/usr/bin/env python3
"""
Module with function named index_range that takes two integer
arguments page and page_size.
The function return a tuple of size two containing
a start index and an end index corresponding to the range
of indexes to return in a list for those particular pagination
parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function named that return page and number of pages

    Args:
    page(int) -- an integer input for page
    page_size -- an integer params for page size
    Return: return a tuple of page and page size
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)

