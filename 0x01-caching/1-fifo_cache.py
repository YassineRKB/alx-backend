#!/usr/bin/env python3
"""module for task 1"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """doc fot fifo cache class"""
    def __init__(self):
        """doc for constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """doc for put method"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                self.cache_data.pop(first)
                print("DISCARD: {}".format(first))

    def get(self, key):
        """doc for get method"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
