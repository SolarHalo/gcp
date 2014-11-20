'''
Created on 2014-10-30

@author: shiwei
'''
from xml.sax import ContentHandler
from lib.gcp.entity.GcpGame import GcpGame
from lib.gcp.util.Logger import LoggerFactory
import xml.sax
from conf import Config
from lib.gcp.handler.DaoHandler import DaoHandler
from lib.core.TaskRun import TaskRun
import time

class AlawarEntityResolver(xml.sax.handler.EntityResolver):
    def resolveEntity(self, publicId, systemId):
        configs = Config.getConfig()
        return configs['game.alawar']['dtd']+systemId
    

class AlawarDecode(ContentHandler):  
    
    logger = LoggerFactory.getLogger()
    
    batchSize = 100
    
    baseBuffer = None;
    
    counter = 0
    
    buf = ''
    
    entity = None
    
    conf = None
    filename = None
    source = None
    def __init__(self,conf,filename,source):
        self.conf = conf
        self.filename = filename
        self.source = source
        
        configs = Config.getConfig()
        self.batchSize = configs['sys']['db.batch.size']

    def startDocument(self):
        self.buf = ''
        self.baseBuffer = []
        
    def endDocument(self):  
        self.logger.info( 'game===counter:%d  , %s ' % (self.counter,self.source));
        if len(self.baseBuffer) > 0:
            dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
            TaskRun.getInstance().submit(dao)

    def startElement(self, name, attrs):  
        self.buf = ''
        if name == 'Property':
            self.Code = attrs['Code']
        elif name == 'Image':
            self.ImageType = attrs['Type']
        elif name == 'Screenshot':
            self.Screenshot = attrs['Type'] + attrs['ID']
            
        elif 'Item' == name:
            self.entity = GcpGame()
            self.entity.gameId = attrs['ID']
            self.counter = self.counter + 1
            
    def endElement(self, name):  
        if self.entity is None:
            return 
        elif 'Property' == name:
            if 'ReleaseDate' == self.Code:
                try:
                    if self.buf is not None and self.buf != '':
                        self.entity.releasedate = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(self.buf,'%Y-%m-%d %H:%M:%S'))
                except Exception , e:
                    self.logger.error("releasedate error %s , %s!"%(self.buf,self.source))
                    self.logger.error(e);
            elif 'SystemRequirements' == self.Code:
                self.entity.systemreq =  self.buf
            elif 'Description45' == self.Code:
                self.entity.shortdesc = self.buf
            elif 'Description80' == self.Code:
                self.entity.meddesc = self.buf
            elif 'Description450' == self.Code:
                if self.buf is not None and self.buf != '':
                    self.entity.longdesc = self.buf
            elif 'Description2000' == self.Code:
                if self.buf is not None and self.buf != '':
                    self.entity.longdesc = self.buf
            elif 'FullVersionFeatures' == self.Code:
                if self.buf is None or self.buf == '':
                    return 
                values = self.buf.split("</li><li>")
                leng = len(values)
                index = -1;
                if leng > 0:
                    for value in values:
                        index += 1
                        value = value.replace('<ul><li>','').replace('</li></ul>','')
                        if index == 0:
                            self.entity.bullet1 = value
                        elif index == 1:
                            self.entity.bullet2 = value
                        elif index == 2:
                            self.entity.bullet3 = value
                        elif index == 3:
                            self.entity.bullet4 = value
                        elif index == 4:
                            self.entity.bullet5 = value
            elif 'OrderUrl' == self.Code:
                if self.buf is None or self.buf == '':
                    return
                self.entity.buyurl = self.buf
            elif 'Embed' == self.Code:  # rewrite
                self.entity.downloadiframe = self.buf
            elif 'SwfHeight' == self.Code:
                self.entity.gamesize = self.buf
            elif 'SymbolCode' == self.Code:
                self.entity.foldername = self.buf
            self.Code = None
        
        elif 'Image' == name:
            if 'icon44x44' == self.ImageType:
                self.entity.imgSmall = self.buf
            elif 'icon44x44bg' == self.ImageType and self.entity.imgSmall is None:
                self.entity.imgSmall = self.buf
            elif 'con100x100' == self.ImageType:
                self.entity.imgMed = self.buf
            elif 'con100x100bg' == self.ImageType and self.entity.imgMed is None:
                self.entity.imgMed = self.buf
            elif 'logo190x140' == self.ImageType:
                self.entity.imgFeature = self.buf
            elif 'banner586x152' == self.ImageType:
                self.entity.imgSubfeature = self.buf
            self.ImageType = None
            
        elif 'Screenshot' == name:
            if 'small0' == self.Screenshot:
                self.entity.imgThumb1 = self.buf
            elif 'small1' == self.Screenshot:
                self.entity.imgThumb2 = self.buf
            elif 'small2' == self.Screenshot:
                self.entity.imgThumb3 = self.buf
            elif 'big0' == self.Screenshot:
                self.entity.imgScreen1 = self.buf
            elif 'big1' == self.Screenshot:
                self.entity.imgScreen2 = self.buf
            elif 'big2' == self.Screenshot:
                self.entity.imgScreen3 = self.buf
            self.Screenshot = None
            
        elif 'Name' == name:
            self.entity.gameName = self.buf
        elif 'File' == name:
            self.entity.downloadurl = self.buf
        elif 'Item' == name:
            self.baseBuffer.append(self.entity)
            if len(self.baseBuffer) >= self.batchSize:
                self.logger.info( 'go to dao :%d  , %s ' % (len(self.baseBuffer),self.source));
                dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
                TaskRun.getInstance().submit(dao)
                self.baseBuffer = []
        
    def characters(self, content):  
        self.buf += content
