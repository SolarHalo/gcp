'''
Created on 2014-11-1

@author: tiamsw
'''
from lib.gcp.util.Dbutil import Dbutil
from lib.gcp.entity.GcpGame import GcpGame

if __name__ == '__main__':
    
    game = GcpGame()
    dbutil = Dbutil()
    game.gameId = "fdsafd"
    game.gameName = None
    
    sql = " insert into test(id,name) values (%s,%s)"
    arg = (game.gameId,
           game.gameName)
    args = [arg,arg]
    dbutil.insertPrepared(sql, arg);
    
    dbutil.close()
    pass