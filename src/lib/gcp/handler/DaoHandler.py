'''
Created on 2014-10-30

@author: shiwei
'''
from lib.gcp.util.Logger import LoggerFactory
from lib.gcp.util.Dbutil import Dbutil
from lib.gcp.util.GcpConstant import GcpConstant
from conf import Config
import time


class DaoHandler(object):
    
    logger = LoggerFactory.getLogger()
    
    filename = None
    cfg = None 
    data = None 
    source = None
    dbutil = None
    
    insertGameSql = 'insert into game(game_id,game_name,family,genre_name,shortdesc,meddesc,\
        longdesc,price,gamerank,releasedate,gamesize,language,site,gametype,systemreq,\
        bullet1,bullet2,bullet3,bullet4,bullet5,img_small,img_med,img_subfeature,img_feature,img_thumb1,\
        img_thumb2,img_thumb3,img_screen1,img_screen2,img_screen3,video,flash,downloadurl,\
        buyurl,downloadiframe,buyiframe,foldername) \
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    selectGameSql = "select game_id c from game where game_id = %s and site = %s"
    
    insertFeatureSql = 'insert into game_feature(g_id,game_id,language,site,gametype,hasdwfeature,dwwidth,dwheight,gamerank,releasedate) \
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    
    selectFeatureSql = 'SELECT f.id AS fid ,g.id AS gid FROM game g LEFT JOIN game_feature f ON g.id = f.g_id WHERE g.game_id = %s AND g.site = %s'
    
    
    insertCatchSql = 'insert into game_catch(g_id,game_id,language,site,gametype,logo_url,images_med,tagline,offer_start_date,offer_end_date,link,price) \
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    
    selectCatchSql = 'SELECT c.id AS cid ,g.id AS gid FROM game g LEFT JOIN game_catch c ON g.id = c.g_id WHERE g.game_id = %s AND g.site = %s'
    
    insertDailySql = 'insert into game_daily(g_id,game_id,language,site,gametype,content,title,link,category,description,pub_date) \
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    
    selectDailySql = 'SELECT d.id AS did ,g.id AS gid FROM game g LEFT JOIN game_daily d ON g.id = d.g_id WHERE g.game_id = %s AND g.site = %s'
    
    

    def __init__(self,filename,cfg,data,source):
        self.data = data
        self.dbutil = Dbutil()
        self.cfg = cfg;
        self.source = source
        self.filename = filename
        
    def execute(self):
        DaoHandler.logger.info("Start insert db length %d , %s , %s"%(len(self.data),self.source,self.cfg))
        buf = []
        
        insert = None;
        lan = None
        gametype = None
        if self.source == GcpConstant.Source.Bigfish:
            lan = self.cfg['locale']
            gametype = self.cfg['gametype']
        else:
            lan = self.cfg['locale']
            gametype = 'pc'
                
        if self.cfg['table'] == 'game':
            insert = DaoHandler.insertGameSql
            for obj in self.data:
                try:
                    rows = self.dbutil.selectRowsPrepared(DaoHandler.selectGameSql, (obj.gameId,self.source))
                    if len(rows) > 0:
                        continue
                    obj.site = self.source
                    obj.language = lan
                    obj.gametype = gametype
                    buf.append((
                        obj.gameId,obj.gameName,obj.family,obj.genreName,obj.shortdesc,
                        obj.meddesc,obj.longdesc,obj.price,obj.gamerank,obj.releasedate,
                        obj.gamesize,obj.language,obj.site,obj.gametype,obj.systemreq,
                        obj.bullet1,obj.bullet2,obj.bullet3,obj.bullet4,obj.bullet5,
                        obj.imgSmall,obj.imgMed,obj.imgSubfeature ,obj.imgFeature,obj.imgThumb1,
                        obj.imgThumb2,obj.imgThumb3,obj.imgScreen1,obj.imgScreen2,obj.imgScreen3,
                        obj.video,obj.flash,obj.downloadurl,obj.buyurl,obj.downloadiframe,obj.buyiframe,obj.foldername
                     ))
                    
                except Exception , e:
                    DaoHandler.logger.error("Prepare insert db data error , length %d , %s !"%(len(self.data),self.source))
                    DaoHandler.logger.exception(e)
        elif self.cfg['table'] == 'game_feature':
            insert = DaoHandler.insertFeatureSql
            for obj in self.data:
                try:
                    rows = self.dbutil.selectRowsPrepared(DaoHandler.selectFeatureSql,(obj.gameId,self.source))
                    if len(rows) <= 0:
                        continue
                    else: 
                        obj.gId = rows[0][1]
                        obj.id = rows[0][0]
                    if obj.id is not None:
                        continue
                    
                    obj.site = self.source
                    obj.language = lan
                    obj.gametype = gametype
                    buf.append((obj.gId,obj.gameId,obj.language,obj.site,obj.gametype,obj.hasdwfeature,obj.dwwidth,obj.dwheight,obj.gamerank,obj.releasedate))
                except Exception , e:
                    DaoHandler.logger.error("Prepare insert db data error , length %d , %s !"%(len(self.data),self.source))
                    DaoHandler.logger.exception(e)     
        elif self.cfg['table'] == 'game_catch':
            insert = DaoHandler.insertCatchSql
            for obj in self.data:
                try:
                    rows = self.dbutil.selectRowsPrepared(DaoHandler.selectCatchSql,(obj.gameId,self.source))
                    if len(rows) <= 0:
                        continue
                    else: 
                        obj.gId = rows[0][1]
                        obj.id = rows[0][0]
                    if obj.id is not None:
                        continue
                    
                    obj.site = self.source
                    obj.language = lan
                    obj.gametype = gametype
                    buf.append((obj.gId,obj.gameId,obj.language,obj.site,obj.gametype,
                                obj.logoUrl,obj.imagesMed,obj.tagline,obj.offerStartDate,obj.offerEndDate,obj.link,obj.price))
                except Exception , e:
                    DaoHandler.logger.error("Prepare insert db data error , length %d , %s !"%(len(self.data),self.source))
                    DaoHandler.logger.exception(e)
        elif self.cfg['table'] == 'game_daily':
            insert = DaoHandler.insertDailySql
            for obj in self.data:
                try:
                    rows = self.dbutil.selectRowsPrepared(DaoHandler.selectDailySql,(obj.gameId,self.source))
                    if len(rows) <= 0:
                        continue
                    else: 
                        obj.gId = rows[0][1]
                        obj.id = rows[0][0]
                    if obj.id is not None:
                        continue
                    
                    obj.site = self.source
                    obj.language = lan
                    obj.gametype = gametype
                    buf.append((obj.gId,obj.gameId,obj.language,obj.site,obj.gametype,
                                obj.content,obj.title,obj.link,obj.category,obj.description,obj.pubDate))
                except Exception , e:
                    DaoHandler.logger.error("Prepare insert db data error , length %d , %s !"%(len(self.data),self.source))
                    DaoHandler.logger.exception(e)
                                
        #==========================================
        
        try:
            if len(buf) > 0:
                self.dbutil.insertPrepared(insert,buf)
        except Exception , e:
            DaoHandler.logger.error("Insert db length %d , %s error !"%(len(self.data),self.source))
            DaoHandler.logger.exception(e)
            # insert batch exception, for single
            for single in buf:
                try:
                    self.dbutil.insertPrepared(insert,single)
                except Exception , exp:
                    singleTxt = ""
                    for sin in single:
                        if sin is None:
                            sin = ""
                        singleTxt = singleTxt+"'%s'|"% sin
                    DaoHandler.logger.error("Insert single error ! %s"%singleTxt)
                    DaoHandler.logger.exception(exp)
        finally:
            DaoHandler.logger.info("End insert db length %d , %s  %s end !"%(len(self.data),self.source,self.filename))
            self.dbutil.close()
            
            