#!/usr/bin/env python3
""" 11-schools_by_topic.py """

def schools_by_topic(mongo_collection, topic):
    """Return a list of schools containing the given topic in their 'topics' field."""
    if mongo_collection is None or not topic:
        return []
    return list(mongo_collection.find({ "topics": topic }))