#!/usr/bin/env python3
"""module for task 0"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class doc"""
    def put(self, key, item):
        """doc for put method"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """doc for get method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
