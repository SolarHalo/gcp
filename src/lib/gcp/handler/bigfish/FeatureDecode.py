'''
Created on 2014-11-3

@author: tiamsw
'''

from xml.sax import ContentHandler
from lib.gcp.entity.GcpGameFeature import GcpGameFeature
from lib.gcp.util.Logger import LoggerFactory
import xml.sax
from conf import Config
from lib.gcp.handler.DaoHandler import DaoHandler
from lib.core.TaskRun import TaskRun
import time

class FeatureDecode(ContentHandler):
    
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
        FeatureDecode.logger.info("Decode file[%s] source[%s] !"%(self.filename,self.source))
        
    def endDocument(self):  
        FeatureDecode.logger.info("game===counter:%d" % self.counter);
        if len(self.baseBuffer) > 0:
            dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
            TaskRun.getInstance().submit(dao)
            
    def startElement(self, name, attrs):
        self.buf = ''
        if 'game' == name:
            self.entity = GcpGameFeature()
            self.entity.gametype = self.conf['gametype']
            self.counter = self.counter + 1
            
    def endElement(self, name):
        if name == 'gameid':
            self.entity.gameId = self.buf
        elif name == 'hasdwfeature':
            self.entity.hasdwfeature = self.buf
        elif name == 'dwwidth':
            self.entity.dwwidth = self.buf
        elif name == 'dwheight':
            self.entity.dwheight = self.buf
        elif name == 'gamerank':
            self.entity.gamerank = self.buf
        elif name == 'releasedate' and self.buf is not None and self.buf != '':
            try:
                self.entity.releasedate = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(self.buf,'%Y-%m-%d %H:%M:%S'))
            except Exception , e:
                self.logger.error("releasedate error %s , %s!"%(self.buf,self.source))
                self.logger.error(e);
        elif 'game' == name:
            self.baseBuffer.append(self.entity)
            if len(self.baseBuffer) >= FeatureDecode.batchSize:
                dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
                TaskRun.getInstance().submit(dao)
                self.baseBuffer = []
        
    def characters(self, content):  
        self.buf += content
