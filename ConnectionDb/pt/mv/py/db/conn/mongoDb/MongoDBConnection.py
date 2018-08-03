'''
Created on Aug 2, 2018

@author: michel.valentin
'''
from pt.mv.py.db.conn import Connection
from pymongo import MongoClient


class MongoDbConnection(Connection):

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