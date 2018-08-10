'''
Created on Aug 2, 2018

@author: michel.valentin
'''
from pymongo import MongoClient
from pt.mv.py.db.conn.ConnectionDB import ConnectionDB


class MongoDbConnection(ConnectionDB):
    db = ''

    def __init__(self, host, port, user, passw):
        self.host = host
        self.port = port
        self.user = user
        self.passw = passw
    
    '''
    Overwrite the super-class 
    '''
    def openConnection(self):
        self.conn = MongoClient(self.host, self.port)
        
    
    def createOrConnectDB(self, dbName):
        self.db = self.conn[dbName]
        