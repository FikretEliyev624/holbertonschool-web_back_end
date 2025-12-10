#!/usr/bin/env python3
""" 10-update_topics.py """

def update_topics(mongo_collection, name, topics):
    """Update the 'topics' field of all documents with the given school name."""
    if mongo_collection is None or not name or not isinstance(topics, list):
        return
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )