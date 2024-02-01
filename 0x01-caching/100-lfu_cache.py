#!/usr/bin/env python3
"""module for task 5"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """doc for LFU cache class"""
    def __init__(self):
        """doc for constructor"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.key_usage = {}

    def put(self, key, item):
        """doc for put method"""
        if key is not None and item is not None:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key = min(self.key_usage, key=self.key_usage.get)
                self.cache_data.pop(lfu_key)
                self.key_usage.pop(lfu_key)
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            self.key_usage[key] = 0
        else:
            return

    def get(self, key):
        """doc for get method"""
        try:
            if key is not None and key in self.cache_data:
                self.key_usage[key] += 1
            return self.cache_data[key]
        except KeyError:
            return None
