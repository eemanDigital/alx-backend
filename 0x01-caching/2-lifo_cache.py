#!/usr/bin/env python3
"""
Last-In First-Out Caching Module
This module defines a caching mechanism that uses
a Last-In First-Out (LIFO) strategy for item removal
when the cache limit is reached. The LIFOCache class
extends the BaseCaching class.
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Cache Class

    Represents a caching mechanism that allows storing
    and retrieving items using a dictionary
    with a LIFO-based eviction strategy.
    Inherits from the BaseCaching class.
    """

    def __init__(self):
        """
        Initialization Method

        Initializes the LIFO cache by calling the constructor
          of the parent class and creating
        an ordered dictionary to keep track of cached
        items' insertion order.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Put Method
        Adds an item to the cache using a LIFO strategy.

        Args:
            key: The key for the item to be stored.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            # Evict the oldest item (LIFO eviction) if cache
            # size exceeds the maximum allowed
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Get Method

        Retrieves an item from the cache using its key.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The retrieved item if found, otherwise None.
        """
        return self.cache_data.get(key, None)
