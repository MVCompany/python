'''
Created on Aug 3, 2018

@author: michel.valentin

This class have goals to be a interface for the persistence objects. 
 @attention: The methods must be implement of:
     1) insert
     2) merge
     3) delete
     4) find
That object is just a reference and if needs others methods can be created.

@param connectionDb:Connection is required. 
@param objectType:Entity is required.
'''
from connFramework.ConnectionDB import ConnectionDB
from daoFramework.dao.entity.Entity import Entity

class Dao(object):
    conn = ''
    obType = ''
    
    '''
    The construct method.
    @param connectionDb a type based in pt.mv.py.db.conn.Connection; 
    @param objectType a type based in daoFramework.dao.entity.Entity;
    '''
    def __init__(self, connectionDb:ConnectionDB, objectType:Entity):
        self.conn = connectionDb
        self.obType = objectType
    
    '''
    Insert the object received
    @param objectType a type based in daoFramework.dao.entity.Entity;
    '''
    def insert(self, objectType:Entity):
        return

    '''
    This method will update the object with this exist or insert. 
    @param objectType a type based in daoFramework.dao.entity.Entity;
    '''        
    def merge(self, objectType:Entity):
        return
    
    '''
    For this method is expected the object where the index to delete.
    @param objectType a type based in daoFramework.dao.entity.Entity;
    '''
    def delete(self, objectType:Entity):
        return
    
    '''
    For this method is expected a dictionary with the key as the column and value the 
    value to filter.
    @param filterDictionary a type Dictionary are expected;
    '''
    def find(self, filterDictionary):
        return object
    
    '''
    Return the type of the entity.
    '''
    def getType(self):
        return self.obType