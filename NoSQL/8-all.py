#!/usr/bin/env python3
"""lists all documents in a collection"""


def list_all(mongo_collection):
    """returns list of all documents in a collection"""
    return list(mongo_collection.find()) or []
#!/usr/bin/env python3
"""lists all documents in a collection"""


def list_all(mongo_collection):
    """returns list of all documents in a collection"""
    return list(mongo_collection.find()) or []
