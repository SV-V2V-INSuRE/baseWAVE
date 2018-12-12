import pymongo

class Database:
    def __init__(self):
        #mongo_url = "mongodb://localhost:27017/"
        #self.mongo = pymongo.MongoClient(mongo_url)
        #self.db = self.mongo["wave"]
        self.db = dict()

    def saveCert(cert):
        db[cert.hash] = cert

    def findCert(hash)
        pass
