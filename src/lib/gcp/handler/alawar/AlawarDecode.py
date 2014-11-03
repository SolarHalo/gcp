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
        return Config.configs['game.alawar']['dtd']+systemId
    

class AlawarDecode(ContentHandler):  
    
    logger = LoggerFactory.getLogger()
    
    batchSize = Config.configs['sys']['db.batch.size']
    
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
            elif 'Description80' == self.Code:
                self.entity.shortdesc = self.buf
            elif 'Description450' == self.Code:
                self.entity.meddesc = self.buf
            elif 'Description2000' == self.Code:
                self.entity.longdesc = self.buf
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
        elif 'Item' == name:
            self.baseBuffer.append(self.entity)
            if len(self.baseBuffer) >= AlawarDecode.batchSize:
                self.logger.info( 'go to dao :%d  , %s ' % (len(self.baseBuffer),self.source));
                dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
                TaskRun.getInstance().submit(dao)
                self.baseBuffer = []
        
    def characters(self, content):  
        self.buf += content