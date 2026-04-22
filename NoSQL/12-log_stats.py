#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs

    num_logs = db.nginx.count_documents({})
    print(f"{num_logs} logs")

    print("Methods:")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for i in method:
        count = db.nginx.count_documents({"method": i})
        print(f"\tmethod {i}: {count}")

    status_check = db.nginx.count_documents(({"method": "GET",
                                            "path": "/status"}))
    print(f"{status_check} status check")
