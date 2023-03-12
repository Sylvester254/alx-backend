#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
      - functions that put and get values to/from cache according to LFU algorithm
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.lfu_keys = []
        self.frequency = {}

    def update_lfu_keys(self, key):
        """ Update LFU keys list and frequency of accessed keys
        """
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1
        if key in self.lfu_keys:
            self.lfu_keys.remove(key)
        self.lfu_keys.append(key)
        self.lfu_keys.sort(key=lambda k: self.frequency[k])

    def evict(self):
        """ Discard the least frequency used item
        """
        min_frequency = min(self.frequency.values())
        lfu_items = [k for k, v in self.frequency.items() if v == min_frequency]
        if len(lfu_items) == 1:
            key = lfu_items[0]
        else:
            key = self.lfu_keys[0]
        del self.cache_data[key]
        del self.frequency[key]
        self.lfu_keys.remove(key)
        print("DISCARD: {}".format(key))

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            self.evict()
        self.cache_data[key] = item
        self.update_lfu_keys(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.update_lfu_keys(key)
        return self.cache_data[key]
