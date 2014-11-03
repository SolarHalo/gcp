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
        DailyDecode.logger.info("Decode file[%s] source[%s] !"%(self.filename,self.source))
        
    def endDocument(self):  
        DailyDecode.logger.info("game===counter:%d" % self.counter);
        if len(self.baseBuffer) > 0:
            dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
            TaskRun.getInstance().submit(dao)
            
    def startElement(self, name, attrs):
        self.buf = ''
        ''''
        '''
            
    def endElement(self, name):  
        '''
        '''
        
    def characters(self, content):  
        self.buf += content

        