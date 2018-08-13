'''

Created on Aug 6, 2018

@author: michel.valentin

This object have goals to be the Entity base from all Entities of persistent DB.

'''
from abc import abstractmethod


class Entity(object):
    dbname = ''
    id = ''
    entityName = ''
    
    '''
    Constructor
    '''
    def __init__(self, dbName, entityName):
        self.dbname = dbName
        self.entityName = entityName

    def getId(self):
        return id  
    
    def getDictionary(self):
        return self.__dict__
    
    '''
    Method receive a row from mongoDb and cast for the object.
    '''
    def setEntityByDictionary(self, dictionaryValye:dict):
        self.__dict__.update(dictionaryValye)
        return self
    
    '''
    This abstract method haveGoals to create a empty object.
    '''
    @abstractmethod
    def createEmpty(self):
        return self(self, '','')
    
    '''
    Method receive a result from mongoDb and cast for a list of object<Entity>.
    '''
    def getListByResult(self, dictionaryValye:dict):
        list = []
        if (dictionaryValye.count() > 0):
            for ob in dictionaryValye:
                ent = self.createEmpty()                
                list.append(ent.setEntityByDictionary(ob))
        return list