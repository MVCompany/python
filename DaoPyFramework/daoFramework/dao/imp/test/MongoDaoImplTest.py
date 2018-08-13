'''
Created on Aug 7, 2018

@author: michel.valentin

That class have the goals to validate the Dao framework.
It just validate a Mongo connection and DDL and DML.

'''
from daoFramework.dao.imp.MongoDaoImpl import MongoDaoImpl
from daoFramework.dao.imp.test.EntityTest import EntityTest
from connFramework.mongoDb.MongoDBConnection import MongoDbConnection

class MongoDaoImplTest(MongoDaoImpl):
        
    def __init__(self):
        self.conn = MongoDbConnection('localhost',27017 , '', '')
        self.obType =  EntityTest()
        self.setCollectionInDb()
        

'''
This method will insert a row in mongoDb
'''    
def insertInMongo():
    #create the DaoImpl 
    mt = MongoDaoImplTest()
    
    #create a test object to insert
    ent = EntityTest()
    ent.testName = 'TestDaoImpl'
    ent.value = 1
   
    ent = mt.insert(ent)    
    
'''
This method select a row in mongoDb
'''
def selectInMongo():
    #create the DaoImpl 
    mt = MongoDaoImplTest()
    
    result = mt.find({})
    
    i= 0
    for ent in result:
        print(ent.getDictionary())
    
    return result
    
'''
This method insert or update the row in mongoDb
'''
def mergeInMongo():
    result = selectInMongo()
    mt = MongoDaoImplTest()
     
    i= 0
    for ent in result:
        ent.testName = str(i) + '_TestDaoImpl'
        mt.merge(ent)
        i += 1
        
'''
This method will delete all rows in mongoDb
'''
def deleteInMongo():
    result = selectInMongo()
    mt = MongoDaoImplTest()
    
    print('Rows before delete in db: ' + str(mt.collectionDao.count())) 
    
    i= 0
    for ent in result:
        mt.delete(ent)
        
    print('Rows after in db: ' + str(mt.collectionDao.count()))

'''
execute test
'''
if __name__ == '__main__':
    insertInMongo()
    selectInMongo()
    mergeInMongo()
    deleteInMongo()