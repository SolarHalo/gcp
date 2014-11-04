'''
Created on 2014-11-3

@author: tiamsw
'''

from xml.sax import ContentHandler
from lib.gcp.entity.GcpGame import GcpGame
from lib.gcp.util.Logger import LoggerFactory
import xml.sax
from conf import Config
from lib.gcp.handler.DaoHandler import DaoHandler
from lib.core.TaskRun import TaskRun
from lib.gcp.entity.GcpGameDaily import GcpGameDaily
import time

class DailyDecode(ContentHandler):
    
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
        DailyDecode.logger.info("game===counter:%d" % self.counter);
        if len(self.baseBuffer) > 0:
            dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
            TaskRun.getInstance().submit(dao)
            
    def startElement(self, name, attrs):
        self.buf = ''
        if 'item' == name:
            self.entity = GcpGameDaily()
            self.entity.gametype = self.conf['gametype']
            self.entity.content = self.conf['content']
            self.counter = self.counter + 1
            
    def endElement(self, name):
        if self.entity is None:
            return
        if name == 'title':
            self.entity.title = self.buf
        elif name == 'guid':
            self.entity.gameId = self.buf
        elif name == 'link':
            self.entity.link = self.buf
        elif name == 'category':
            self.entity.category = self.buf
        elif name == 'description':
            self.entity.description = self.buf
        elif name == 'pubDate':
            try:
                if self.buf is not None and self.buf != '':
                    self.entity.pubDate = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(self.buf[:-6],'%a, %m %b %Y %H:%M:%S'))
            except Exception , e:
                DailyDecode.logger.error("pubDate error %s , %s!"%(self.buf,self.source))
                DailyDecode.logger.error(e)
        elif 'item' == name:
            self.baseBuffer.append(self.entity)
            if len(self.baseBuffer) >= DailyDecode.batchSize:
                dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
                TaskRun.getInstance().submit(dao)
                self.baseBuffer = []
            self.entity = None
        
    def characters(self, content):  
        self.buf += content

        