'''
Created on 2014-12-3

@author: tiamsw
'''
from lib.gcp.util.Dbutil import Dbutil
from lib.gcp.util.Logger import LoggerFactory
import jieba
import jieba.analyse

class TagHandler:
    
    logger = LoggerFactory.getLogger()
    
    def __init__(self):
        '''
        Constructor
        '''
    def getGames(self):
        
        games = []
        dbutil = None
        try:
            index = 0;
            pageSize = 100;
            
            dbutil = Dbutil()
            rows = dbutil.selectRows("select count(id) from game WHERE id NOT IN (SELECT DISTINCT obj_id FROM relations ) ")
            count = rows[0][0]
            
            while(index <= count):
                rows = dbutil.selectRows("select id,game_name from game WHERE id NOT IN (SELECT DISTINCT obj_id FROM relations ) limit %d , %d "%(index,pageSize))
                index = index + pageSize
                for row in rows:    
                    games.append([row[0],row[1]])
                
        except Exception , e:
            TagHandler.logger.exception(e)
        finally:
            if dbutil is not None:
                dbutil.close() 
        return games 
    
    def saveTags(self,tags):
        dbutil = None
        sql = " insert into tags(tag_name) values(%s) "
        pageSize = 4000;
        
        tags = set(tags)
        
        try:
            dbutil = Dbutil()
            
            buf = []
            for tag in tags:
                buf.append((tag))
                if len(buf) > pageSize:
                    dbutil.insertPrepared(sql, buf)
                    TagHandler.logger.info("Insert tags %d"%pageSize)
                    buf = []
            
            if len(buf) > 0:
                dbutil.insertPrepared(sql, buf)
        except Exception , e:
            TagHandler.logger.exception(e)
        finally:
            if dbutil is not None:
                dbutil.close() 
    def saveRelations(self,relations):
        dbutil = None
        sql = " insert into relations(tag_id,obj_id) values(%s,%s) "
        pageSize = 4000;
        
        try:
            dbutil = Dbutil()
            
            buf = [];
            for relation in relations:
                buf.append((int(relation[0]),int(relation[1])))
                if len(buf) > pageSize:
                    dbutil.insertPrepared(sql, buf)
                    TagHandler.logger.info("Insert relations %d"%pageSize)
                    buf = []
                    
            if len(buf) > 0:
                dbutil.insertPrepared(sql, buf)
        except Exception , e:
            TagHandler.logger.exception(e)
        finally:
            if dbutil is not None:
                dbutil.close() 
                
    def getTags(self):
        tags = {}
        dbutil = None
        try:
            index = 0;
            pageSize = 1000;
            
            dbutil = Dbutil()
            rows = dbutil.selectRows("SELECT COUNT(tag_id) FROM tags")
            count = rows[0][0]
            
            while(index <= count):
                rows = dbutil.selectRows("SELECT tag_id, tag_name FROM tags limit %d , %d "%(index,pageSize))
                index = index + pageSize
                for row in rows:    
                    tags[row[1]] = int(row[0])
                
        except Exception , e:
            TagHandler.logger.exception(e)
        finally:
            if dbutil is not None:
                dbutil.close() 
        return tags
    def getRelations(self):
        relations = {}
        dbutil = None
        try:
            index = 0;
            pageSize = 1000;
            
            dbutil = Dbutil()
            rows = dbutil.selectRows("SELECT COUNT(tag_id) FROM relations")
            count = rows[0][0]
            
            while(index <= count):
                rows = dbutil.selectRows("SELECT tag_id, obj_id FROM relations limit %d , %d "%(index,pageSize))
                index = index + pageSize
                for row in rows:    
                    relations[row[0]] = int(row[1])
                
        except Exception , e:
            TagHandler.logger.exception(e)
        finally:
            if dbutil is not None:
                dbutil.close() 
        return relations 
    
    
    def parse(self,content):
        return jieba.analyse.extract_tags(content, topK = 4,)
    
    def execute(self):
        
        #get games
        games = self.getGames()
        
        #game tags
        tagsCache = self.getTags()
        
        #save tags
        tags = []
        for game in games:
            gameTags = self.parse(game[1])
            for gameTag in gameTags:
                if not tagsCache.has_key(gameTag):
                    tags.append(gameTag)
        self.saveTags(tags)
        
        
        #game tags
        tagsCache = self.getTags()
        relationsCache = self.getRelations()
        
        relations = []
        for game in games:
            gameTags = self.parse(game[1])
            for gameTag in gameTags:
                if tagsCache.has_key(gameTag):
                    tagId = tagsCache.get(gameTag)
                    if relationsCache.get(tagId) != game[0]:
                        relations.append([tagId,int(game[0])])
        self.saveRelations(relations)
        
            
                  
        
        
        
        