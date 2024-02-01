#!/usr/bin/env python3
"""module for task 3"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """doc for LRU cache class"""
    def __init__(self):
        """doc for constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """doc for put method"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    lru_key, _ = self.cache_data.popitem(True)
                    print("DISCARD:", lru_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item
        else:
            return

    def get(self, key):
        """doc for get method"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
