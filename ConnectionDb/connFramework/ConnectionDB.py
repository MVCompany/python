'''
Created on Aug 2, 2018

@author: michel.valentin

This class have the gols to define the main attributs and methods for a DB connection
For use with your DB just implement ConnectionDB and define the openConnection

For operation DML use the DaoObject and pass for the connection the object 
especialized by this connection.
 
'''
class ConnectionDB(object):
    host = 'localhost'
    port = 999999
    user = 'user'
    passw = 'password'
    conn = ''

    def __init__(self, host, port, user, passw):
        self.host = host
        self.port = port
        self.user = user
        self.passw = passw
    
    def openConnection(self):
        self.conn = object
    
    '''
    This method will return the connectio of your DB.
    '''
    def getConnection(self):
        if (type(self.conn) == str):
            return self.conn
        raise ConnectionError('Connection was not defined!')
        
    def closeConnection(self):
        if (type(self.conn) == str):
            self.conn.close()
        print('Connection closed')