#!/usr/bin/env python3
""" 12-log_stats.py """
from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # 1. Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Methods counts
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. GET /status count
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    main()