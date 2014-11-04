'''
Created on 2014-11-3

@author: tiamsw
'''

from xml.sax import ContentHandler
from lib.gcp.util.Logger import LoggerFactory
import xml.sax
from conf import Config
from lib.gcp.handler.DaoHandler import DaoHandler
from lib.core.TaskRun import TaskRun
from lib.gcp.entity.GcpGameCatch import GcpGameCatch
import time

class CatchDecode(ContentHandler):
    
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
        CatchDecode.logger.info("Decode file[%s] source[%s] !"%(self.filename,self.source))
        
    def endDocument(self):  
        CatchDecode.logger.info("game===counter:%d" % self.counter);
        if len(self.baseBuffer) > 0:
            dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
            TaskRun.getInstance().submit(dao)
            
    def startElement(self, name, attrs):
        self.buf = ''
        if 'game' == name:
            self.entity = GcpGameCatch()
            self.entity.gametype = self.conf['gametype']
            self.counter = self.counter + 1
            
    def endElement(self, name):
        if self.entity is None:
            return 
        if name == 'gameid':
            self.entity.gameId = self.buf
        elif name == 'med':
            self.entity.imagesMed = self.buf
        elif name == 'logo_url':
            self.entity.logoUrl = self.buf
        elif name == 'tagline':
            self.entity.tagline = self.buf
        elif name == 'link':
            self.entity.link = self.buf
        elif name == 'price':
            self.entity.price = self.buf
        elif name == 'offer_start_date' and self.buf is not None and self.buf != '':
            try:
                if self.buf is not None and self.buf != '':
                    self.entity.offerStartDate = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(self.buf[:-6],'%a, %m %b %Y %H:%M:%S'))
            except Exception , e:
                self.logger.error("offer_start_date error %s , %s!"%(self.buf,self.source))
                self.logger.error(e);
            
        elif name == 'offer_end_date' and self.buf is not None and self.buf != '':
            try:
                if self.buf is not None and self.buf != '':
                    self.entity.offerStartDate = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(self.buf[:-6],'%a, %m %b %Y %H:%M:%S'))
            except Exception , e:
                self.logger.error("offer_end_date error %s , %s!"%(self.buf,self.source))
                self.logger.error(e);
        elif 'game' == name:
            self.baseBuffer.append(self.entity)
            if len(self.baseBuffer) >= CatchDecode.batchSize:
                dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
                TaskRun.getInstance().submit(dao)
                self.baseBuffer = []
            self.entity = None
        
    def characters(self, content):  
        self.buf += content
