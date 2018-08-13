'''
Created on Aug 6, 2018

@author: michel.valentin
'''
from daoFramework.dao.Dao import Dao
from connFramework.mongoDb.MongoDBConnection import MongoDbConnection
from daoFramework.dao.entity.Entity import Entity

class MongoDaoImpl(Dao):
    collectionDao = ''
    
    '''
    The construct method.
    @param connectionDb a type based in pt.mv.py.db.conn.Connection; 
    @param objectType a type based in daoFramework.dao.entity.Entity;
    '''
    def __init__(self, connectionDb:MongoDbConnection, objectType:Entity):
        self.conn = connectionDb
        self.obType = objectType
        self.setCollectionInDb()

    '''
    The method wich will start the DB and set the collection for the entity.
    DB name and collection is define on the Entity of this DAO.
    '''    
    def setCollectionInDb(self):
        if (type(self.collectionDao) == str) :
            self.conn.openConnection()
            self.conn.createOrConnectDB(self.obType.dbname)
            self.collectionDao = self.conn.db[self.getType().entityName]
            
        return self.collectionDao
            
    '''
    Insert the object received.
    @param objectType a type based in daoFramework.dao.entity.Entity;
    '''
    def insert(self, objectType:Entity):
        dictFromObj = objectType.getDictionary()
        objectType.id = self.collectionDao.insert_one(dictFromObj)
        return objectType

    '''
    This method will update the object with this exist or insert. 
    @param objectType a type based in daoFramework.dao.entity.Entity;
    '''        
    def merge(self, objectType:Entity):
        return self.collectionDao.save(objectType.getDictionary())
    
    '''
    For this method is expected the object where the index to delete.
    @param objectType a type based in daoFramework.dao.entity.Entity;
    '''
    def delete(self, objectType:Entity):
        return self.collectionDao.remove(objectType.getDictionary())
    
    '''
    For this method is expected aa dictionary with the key as the column and value the 
    value to filter.
    @param filterDictionary a type Dictionary are expected;
    '''
    def find(self, filterDictionary:dict):
        return self.obType.getListByResult(self.collectionDao.find(filterDictionary))
    