#!/usr/bin/env python3
"""
Basic Caching Module

This module defines a basic caching mechanism by
extending the BaseCaching class.
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache Class

    Represents a basic caching mechanism that allows
    storing and retrieving items using a dictionary.
    Inherits from the BaseCaching class.
    """

    def put(self, key, item):
        """
        Put Method

        Adds an item to the cache.

        Args:
            key: The key for the item to be stored.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
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
        return self.cache_data.get(key, None)
