'''
Created on 2013-8-16

@author: Administrator
'''

from conf import Config
import MySQLdb
import time
 
 
class Dbutil: 
    def __init__(self):  
        self.host = Config.configs['db']['db_host']
        self.user = Config.configs['db']['db_user']
        self.pwd = Config.configs['db']['db_pass']
        self.db = Config.configs['db']['db_db']
        self.conn = None
        try:
            self.conn = MySQLdb.Connect(host=self.host, user=self.user, passwd=self.pwd, db=self.db, charset="utf8", use_unicode="True") 
        except MySQLdb.Error, e:
            print e
            print "can't connect database error num %d the desc is %s" % (e[0], e[1])
       
        
    
    def getConn(self, host, user, pwd, db):  
        self.conn = MySQLdb.Connect(host=host, user=user, passwd=pwd, db=db, charset="utf8", use_unicode="True")  
        return self.conn  
      
    def insert(self, sql):
        if self.conn == None:  
            self.conn = self.getConnWithConfig()
            print "the conn is None"
        self.cursor = self.conn.cursor()  
        self.cursor.execute(sql)  
        self.conn.commit() 
         
    def insertPrepared(self, sql, args):
        if self.conn == None:  
            self.conn = self.getConnWithConfig()
            print "the conn is None"
        self.cursor = self.conn.cursor()
        if isinstance(args, list):
            for arg in args:  
                self.cursor.execute(sql,arg)
        else:
            self.cursor.execute(sql,args)
        self.conn.commit() 
        
    def update(self, sql):
        if self.conn == None:  
            self.conn = self.getConnWithConfig()
            print "the conn is None"  
        self.cursor = self.conn.cursor()  
        self.cursor.execute(sql)  
        self.conn.commit()  
    
    def updatePrepared(self, sql,arg):
        if self.conn == None:  
            self.conn = self.getConnWithConfig()
            print "the conn is None"  
        self.cursor = self.conn.cursor()  
        self.cursor.execute(sql,arg)  
        self.conn.commit() 
        
      
    def selectRows(self, sql):
        if self.conn == None:  
            print "sleep 10 ms,when conn =None " 
            time.sleep(50)
            self.conn = self.getConnWithConfig()
            print "the conn is None"  
        self.cursor = self.conn.cursor()  
        self.cursor.execute(sql)  
        self.conn.commit()  
        self.rows = self.cursor.fetchall()  
        self.cursor.close() 
        return self.rows  
    
    def selectRowsPrepared(self, sql,arg):
        if self.conn == None:  
            print "sleep 10 ms,when conn =None " 
            time.sleep(50)
            self.conn = self.getConnWithConfig()
            print "the conn is None"  
        self.cursor = self.conn.cursor()  
        self.cursor.execute(sql,arg)  
        self.conn.commit()  
        self.rows = self.cursor.fetchall()  
        self.cursor.close() 
        return self.rows
      
    def close(self):
        if(self.cursor != None):
            self.cursor.close() 
            self.conn.close() 
if __name__ == '__main__':
    dbutil = Dbutil() 
    rows = dbutil.selectRows("select * from admin_users")
    dbutil.closeConn()
    print  rows
