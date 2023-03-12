#!/usr/bin/python3
"""
This module implements a basic caching system using various algorithms.

Supported algorithms:
    - FIFO
    - LIFO
    - LRU
    - MRU
    - LFU

Classes:
    - BaseCaching: Base class for all caching algorithms.
    - FIFOCache: Implements the FIFO caching algorithm.
    - LIFOCache: Implements the LIFO caching algorithm.
    - LRUCache: Implements the LRU caching algorithm.
    - MRUCache: Implements the MRU caching algorithm.
    - LFUCache: Implements the LFU caching algorithm.
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")