'''
Created on 2014-10-29

@author: tiamsw
'''
import sys, os
reload(sys)

from lib.gcp.util.StaticUtil  import StaticUtil
import gzip
import urllib
from lib.gcp.util.Logger import LoggerFactory
import time

class Download(object):
    
    logger = LoggerFactory.getLogger()
    
    second = 0
    
    '''
    download
    '''
    def __init__(self, url, file_path):
        
        self.url = url
        self.filepath = file_path
        self.second = time.time()
        
    def callbak(self, a, b, c):  
        ''''' 
        @a: all dowwload block num
        @b: data block size
        @c: file size
        '''  
        per = 100.0 * a * b / c  
        if per > 100:  
            per = 100  
        if time.time() - self.second > 10:
            self.logger.info('%.2f%%   =====> file[%s]' % (per,self.filepath))
            self.second = time.time()
        
    def executeDown(self):  
        self.logger.info("#####################now download file %s the time is %s############" % (self.filepath, StaticUtil.getTimeStrForShow()))
        urllib.urlretrieve(self.url, self.filepath, self.callbak)
        self.logger.info("#####################down load file %s over at %s################" % (self.filepath, StaticUtil.getTimeStrForShow()))
    
    def gzipFile(self, newName):
        filePath = self.filepath[:-3] 
        isExists = os.path.exists(filePath) 
        if not isExists:  
            os.makedirs(filePath)
        datefilepath = filePath + "/" + newName
        self.logger.info("#####################now explain the gz file:%s at time is :%s " % (datefilepath, StaticUtil.getTimeStrForShow()))
        g = gzip.GzipFile(mode='rb', fileobj=open(self.filepath, 'rb'))
        open(datefilepath, 'wb').write(g.read())
        self.logger.info("#####################over explain the gz at time is :%s " % (StaticUtil.getTimeStrForShow()))
        return datefilepath
