#!/usr/bin/env python3
"""
First-In First-Out Caching Module
This module defines a caching mechanism that uses
a First-In First-Out (FIFO) strategy for item removal
when the cache limit is reached. The FIFOCache class
extends the BaseCaching class.
"""


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Cache Class

    Represents a caching mechanism that allows storing
    and retrieving items using a dictionary
    with a FIFO-based eviction strategy.
    Inherits from the BaseCaching class.
    """
    def __init__(self):
        """
        Initialization Method
        Initializes the FIFO cache by calling the constructor
        of the parent class and creating
        an ordered dictionary to keep track of cached
        items' insertion order.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Put Method
        Adds an item to the cache using a FIFO strategy.

        Args:
            key: The key for the item to be stored.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        # If cache size exceeds the maximum allowed, remove
        # the oldest item (FIFO eviction)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Get Method Retrieves an item from the cache using its key.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The retrieved item if found, otherwise None.
        """
        return self.cache_data.get(key, None)
