'''
Created on Aug 7, 2018

@author: michel.valentin
'''
from daoFramework.dao.entity.Entity import Entity
from abc import abstractmethod

class EntityTest(Entity):
    testName = ''
    value = ''
   
    def __init__(self):
        self.dbname = 'dbtest'
        self.entityName = 'entityTest'
    
    '''
    This abstract method haveGoals to create a empty object.
    '''
    @abstractmethod
    def createEmpty(self):
        return EntityTest()