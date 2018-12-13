import pymongo

class Database:
    def __init__(self):
        #mongo_url = "mongodb://localhost:27017/"
        #self.mongo = pymongo.MongoClient(mongo_url)
        #self.db = self.mongo["wave"]
        self.db = dict()

    def saveCert(cert):
        db[cert.__hash__()] = cert

    def findCert(hash):
        if self.db.has_key(hash):
            return self.db[hash]
        else:
            return False
