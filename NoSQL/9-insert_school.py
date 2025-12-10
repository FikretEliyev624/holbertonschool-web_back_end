#!/usr/bin/env python3
""" 9-insert_school.py """

def insert_school(mongo_collection, **kwargs):
    """Insert a new document in the collection using kwargs and return the _id."""
    if mongo_collection is None or not kwargs:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id