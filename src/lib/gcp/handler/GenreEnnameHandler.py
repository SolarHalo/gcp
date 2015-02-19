'''
Created on 2014-12-3

@author: tiamsw
'''
from lib.gcp.util.Dbutil import Dbutil
from lib.gcp.util.Logger import LoggerFactory
from conf import Config

class GenreEnnameHandler:
    
    logger = LoggerFactory.getLogger()
    
    config = None ;
    
    def __init__(self):
        '''
        Constructor
        '''
        self.config = Config.getConfig()
        
    def getGames(self):
        
        games = []
        dbutil = None
        try:
            index = 0;
            pageSize = 100;
            
            dbutil = Dbutil()
            rows = dbutil.selectRows("select count(id) from game where genre_enname is null ")
            count = rows[0][0]
            
            while(index <= count):
                rows = dbutil.selectRows("select id,genre_name,language from game  where genre_enname is null  limit %d , %d "%(index,pageSize))
                index = index + pageSize
                for row in rows:    
                    games.append([row[0],row[1],row[2]])
                
        except Exception , e:
            GenreEnnameHandler.logger.exception(e)
        finally:
            if dbutil is not None:
                dbutil.close() 
        return games 
   
    
    def execute(self):
        games = self.getGames()
        try:
            dbutil = Dbutil()
            
            for game in games:
                
                gameId = game[0];
                genreName = game[1];
                language = game[2];
                
                lancfg = self.config['genrelist'][language]
                
                if lancfg is not None:
                    genreType = lancfg[genreName];
                    if genreType is not None:
                        genreEnname = self.config['genrelist'][genreType];
                        if genreEnname is not None:
                            sql = " update game set genre_enname = %s where id= %s" ;
                            dbutil.updatePrepared(sql, (genreEnname,gameId));
                        else:
                            GenreEnnameHandler.self.logger.info("genreType[%s] not config  gameid[%s] , genreName[%s]"%(genreType,gameId ,genreName))
                    else:
                        GenreEnnameHandler.self.logger.info("genreName[%s] config not found in language[%s], gameid[%s] , genreName[%s]"%(genreName,language,gameId ,genreName))
                else:
                    GenreEnnameHandler.self.logger.info("language[%s] config not found , gameid[%s] , genreName[%s]"%(language,gameId ,genreName))
                        
        except Exception , e:
            GenreEnnameHandler.logger.exception(e)
        finally:
            if dbutil is not None:
                dbutil.close()                 
                        
                
            
            
        
        
        
            