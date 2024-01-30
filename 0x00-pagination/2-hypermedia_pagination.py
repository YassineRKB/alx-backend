#!/usr/bin/env python3
"""module for task 2"""
from typing import Tuple, List, Dict
import csv
from math import ceil


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    start = page_size * (page - 1)
    end = page * page_size
    res = (start, end)
    return res


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Finds the correct indexes to paginate dataset correctly"""
        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(page, int) and page > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Finds the correct indexes to paginate dataset correctly"""
        all_pages = ceil(len(self.dataset()) / page_size)
        pageSize = page_size if page < all_pages else 0
        pageData = self.get_page(page, page_size)
        pagePrev = page - 1 if page > 1 else None
        pageNext = page + 1 if page < all_pages else None
        res = {
            "page_size": pageSize,
            "page": page,
            "data": pageData,
            "next_page": pageNext,
            "prev_page": pagePrev,
            "total_pages": all_pages
        }
        return res
