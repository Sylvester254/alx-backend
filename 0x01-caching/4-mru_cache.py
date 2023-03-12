#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
      - caching system with MRU algorithm
    """

    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.access_list = []

    def put(self, key, item):
        """ Add an item in the cache with MRU algorithm
        """
        if key is None or item is None:
            return

        # Update item if it already exists
        if key in self.cache_data:
            self.access_list.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = self.access_list.pop()
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))

        self.access_list.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from cache with MRU algorithm
        """
        if key is None or key not in self.cache_data:
            return None

        self.access_list.remove(key)
        self.access_list.append(key)
        return self.cache_data[key]
