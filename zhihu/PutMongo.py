import pymongo

class putMongo():

    def __init__(self, client='localhost', dbName='zhihu', colName='actors'):
        self.client = pymongo.MongoClient(client)
        self.db = self.client[dbName]
        self.col = self.db[colName] 
      
    def insertData(self, data, page):
        self.col.insert_many(data)
        print('已插入第{}页！'.format(page))
    
    def findData(self, items):

        choosedItems = {}
        for i in items:
            choosedItems[i] = 1

        data = self.col.find({}, choosedItems)
        return data
        



