#!/usr/bin/env python3
"""
Most Recently Used Caching Module
This module defines a caching mechanism that
uses a Most Recently Used (MRU) strategy for item removal
when the cache limit is reached. The MRUCache class
extends the BaseCaching class.
"""


from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Cache Class

    Represents a caching mechanism that allows storing
    and retrieving items using a dictionary
    with an MRU-based eviction strategy.
    Inherits from the BaseCaching class.
    """

    def __init__(self):
        """
        Initialization Method

        Initializes the MRU cache by calling the constructor
        of the parent class and creating
        an ordered dictionary to keep track of cached items'
        insertion order.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Put Method

        Adds an item to the cache using an MRU strategy.

        Args:
            key: The key for the item to be stored.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            # Evict the most recently used item (MRU eviction)
            # if cache size exceeds the maximum allowed
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)

            # Add the new item to the cache and move it to the
            # front
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            # If the key is already in the cache, update the
            # item and move it to the front
            self.cache_data[key] = item

    def get(self, key):
        """
        Get Method

        Retrieves an item from the cache using its key.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The retrieved item if found, otherwise None.
        """
        if key is not None and key in self.cache_data:
            # Move the accessed item to the front (MRU position)
            self.cache_data.move_to_end(key, last=False)

        return self.cache_data.get(key, None)
