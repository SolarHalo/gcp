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
    
    insertSql = 'insert into game(game_id,game_name,family,genre_name,shortdesc,meddesc,\
        longdesc,price,gamerank,releasedate,gamesize,language,site,gametype,systemreq,\
        bullet1,bullet2,bullet3,bullet4,bullet5,img_small,img_med,img_subfeature,img_feature,img_thumb1,\
        img_thumb2,img_thumb3,img_screen1,img_screen2,img_screen3,video,flash,downloadurl,\
        buyurl,downloadiframe,buyiframe,foldername) \
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    repeatSql = "select game_id c from game where game_id = %s and site = %s"

    def __init__(self,filename,cfg,data,source):
        self.data = data
        self.dbutil = Dbutil()
        self.cfg = cfg;
        self.source = source
        self.filename = filename
        
    def execute(self):
        DaoHandler.logger.info("Start insert db length %d , %s , %s"%(len(self.data),self.source,self.cfg))
        
        lan = None
        gametype = None
        if self.source == GcpConstant.Source.Bigfish:
            lan = self.cfg['locale']
            gametype = self.cfg['gametype']
        else:
            lan = self.cfg['locale']
            gametype = 'pc'
        
        buf = []
        for obj in self.data:
            try:
                rows = self.dbutil.selectRowsPrepared(DaoHandler.repeatSql, (obj.gameId,self.source))
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
                DaoHandler.logger.error(e)
        try:
            if len(buf) > 0:
                self.dbutil.insertPrepared(DaoHandler.insertSql,buf)
        except Exception , e:
            DaoHandler.logger.error("Insert db length %d , %s error !"%(len(self.data),self.source))
            DaoHandler.logger.error(e)
            # insert batch exception, for single
            for single in buf:
                try:
                    self.dbutil.insertPrepared(DaoHandler.insertSql,single)
                except Exception , e:
                    singleTxt = ""
                    for sin in single:
                        singleTxt += sin
                    DaoHandler.logger.error("Insert single error ! "+singleTxt)
                    DaoHandler.logger.error(e)
        finally:
            DaoHandler.logger.info("End insert db length %d , %s  %s end !"%(len(self.data),self.source,self.filename))
            self.dbutil.close()
            
            