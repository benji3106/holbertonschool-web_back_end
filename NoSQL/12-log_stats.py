#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total = collection.countDocuments()
    print("{} logs".format(total))

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.countDocuments({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status = collection.countDocuments({"method": "GET", "path": "/status"})
    print("{} status check".format(status))
