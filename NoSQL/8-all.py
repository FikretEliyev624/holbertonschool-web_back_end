#!/usr/bin/env python3
"""8-all.py"""


def list_all(mongo_collection):
    """Return all documents in a collection as a list."""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
