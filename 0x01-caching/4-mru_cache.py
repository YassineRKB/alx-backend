#!/usr/bin/ev python3
"""module for task 4"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """doc for MRU cache class"""
    def __init__(self):
        """doc for constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """doc for put method"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    mru_key = next(reversed(self.cache_data))
                    self.cache_data.pop(mru_key)
                    print("DISCARD:", mru_key)
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=True)
        else:
            return

    def get(self, key):
        """doc for get method"""
        try:
            if key is not None and key in self.cache_data:
                self.cache_data.move_to_end(key, last=True)
            return self.cache_data[key]
        except KeyError:
            return NoneW
