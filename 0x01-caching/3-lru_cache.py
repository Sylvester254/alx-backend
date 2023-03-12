#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        # If the key already exists, update the
        # value and move it to the end of the OrderedDict
        if key in self.cache_data:
            self.cache_data.pop(key)
        # If the cache is full, remove the first (least recently used) item
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discard_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(discard_key))
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key and move it to the end of the OrderedDict
        """
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
