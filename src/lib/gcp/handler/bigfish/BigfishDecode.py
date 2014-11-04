
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

class BigfishEntityResolver(xml.sax.handler.EntityResolver):
    def resolveEntity(self, publicId, systemId):
        return Config.configs['game.bigfish']['dtd'] + systemId
    

class BigfishDecode(ContentHandler):  
    
    logger = LoggerFactory.getLogger()
    
    batchSize = Config.configs['sys']['db.batch.size']
    
    baseBuffer = None;
    
    counter = 0
    
    buffer = ''
    
    entity = None
    
    conf = None
    filename = None
    source = None
    def __init__(self,conf,filename,source):
        self.conf = conf
        self.filename = filename
        self.source = source

    def startDocument(self):
        self.buffer = ''
        self.baseBuffer = []
        self.logger.info("Decode file[%s] source[%s] !"%(self.filename,self.source))
        
    def endDocument(self):  
        self.logger.info( 'game===counter:%d' % self.counter);
        if len(self.baseBuffer) > 0:
            dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
            TaskRun.getInstance().submit(dao)
    def startElement(self, name, attrs):
        self.buffer = ''
        if 'game' == name:
            self.entity = GcpGame()
            self.entity.gametype = self.conf['gametype']
            self.counter = self.counter + 1
        elif name == 'genreid':
            self.entity.genreName = attrs['name']
            
            
    def endElement(self, name):
        if self.entity is None:
            return   
        if name == 'gameid':
            self.entity.gameId = self.buffer
        elif name == 'gamename':
            self.entity.gameName = self.buffer
        elif name == 'family':
            self.entity.family = self.buffer
        elif name == 'shortdesc':
            self.entity.shortdesc = self.buffer
        elif name == 'meddesc':
            self.entity.meddesc = self.buffer
        elif name == 'longdesc':
            self.entity.longdesc = self.buffer
        elif name == 'bullet1':
            self.entity.bullet1 = self.buffer
        elif name == 'bullet2':
            self.entity.bullet2 = self.buffer
        elif name == 'bullet3':
            self.entity.bullet3 = self.buffer
        elif name == 'bullet4':
            self.entity.bullet4 = self.buffer
        elif name == 'bullet5':
            self.entity.bullet5 = self.buffer
        elif name == 'foldername':
            self.entity.foldername = self.buffer
        elif name == 'price':
            self.entity.price = self.buffer
        elif name == 'gamesize':
            self.entity.gamesize = self.buffer
        elif name == 'gamerank':
            self.entity.gamerank = self.buffer
        elif name == 'hasvideo':
            self.entity.video = self.buffer
        elif name == 'hasflash':
            self.entity.flash = self.buffer
        elif name == 'releasedate' and self.buffer is not None and self.buffer != '':
            try:
                self.entity.releasedate = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(self.buffer,'%Y-%m-%d %H:%M:%S'))
            except Exception , e:
                self.logger.error("releasedate error %s , %s!"%(self.buf,self.source))
                self.logger.error(e);
        elif name == 'sysreqos':
            self.entity.systemreq = 'OS: ' + self.buffer 
        elif name == 'sysreqmhz':
            self.entity.systemreq = self.entity.systemreq + ' / CPU: ' + self.buffer 
        elif name == 'sysreqmem':
            self.entity.systemreq = self.entity.systemreq + ' / RAM: ' + self.buffer
        elif name == 'sysreqdx':
            self.entity.systemreq = self.entity.systemreq + ' / DirectX: ' + self.buffer
        elif name == 'sysreqhd':
            self.entity.systemreq = self.entity.systemreq + ' / ' + self.buffer
            
        elif 'game' == name:
            self.baseBuffer.append(self.entity)
            if len(self.baseBuffer) >= BigfishDecode.batchSize:
                dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
                TaskRun.getInstance().submit(dao)
                self.baseBuffer = []
            self.entity = None
                
    def characters(self, content):  
        self.buffer += content
