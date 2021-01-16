import pymongo

class DatabaseService():
    def __init__(self, url, database):
        self.client = pymongo.MongoClient(url)
        self.database = self.client[database]


    def get_collection(self, name):
        return self.database[name]