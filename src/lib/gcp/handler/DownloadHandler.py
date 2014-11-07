'''
Created on 2014-10-30

@author: shiwei
'''

from lib.gcp.util.Download import Download
import lib.gcp.handler.bigfish.FeatureParserHandler
import lib.gcp.handler.alawar.FeatureParserHandler
from lib.gcp.util.GcpConstant import GcpConstant
from lib.core.TaskRun import TaskRun
from conf import Config
from threading import Lock
from lib.gcp.util.StaticUtil import StaticUtil
from lib.gcp.util.Logger import LoggerFactory

class DownloadHandler(object):
    
    logger = LoggerFactory.getLogger()
    
    dowNum = 0
    
    Threads_lock = Lock()
    
    url = None
    
    conf = None
    
    filename = None
    
    source = None
    
    def __init__(self, conf, filename, source):
        self.url = conf['url']
        self.conf = conf
        self.filename = filename
        self.source = source
        
    def execute(self):
        
        StaticUtil.remove(self.filename)
        
        configs = Config.getConfig()
        dowLoadNum = configs['sys']['download.num']
        
        DownloadHandler.Threads_lock.acquire()
        try:
            #self.logger.info("Download Num is %d , MaxNum is %d ."%(DownloadHandler.dowNum,dowLoadNum));
                
            if DownloadHandler.dowNum >= dowLoadNum:
                TaskRun.getInstance().submit(self)
                #self.logger.info("Now file[%s] download go back ."%self.filename);
                return
            DownloadHandler.dowNum += 1
        finally:
            DownloadHandler.Threads_lock.release()

        try:
            
            self.logger.info("Download file[%s] start , %s !"%(self.filename,self.source))
            download = Download(self.url, self.filename)
            download.executeDown();
            
            if self.source == GcpConstant.Source.Bigfish:
                parse = lib.gcp.handler.bigfish.FeatureParserHandler.FeatureParserHandler(self.filename, self.source,self.conf);
                TaskRun.getInstance().submit(parse)
            elif  self.source == GcpConstant.Source.Alawar:
                parse = lib.gcp.handler.alawar.FeatureParserHandler.FeatureParserHandler(self.filename, self.source,self.conf);
                TaskRun.getInstance().submit(parse)
            
        except Exception , e:
            self.logger.error("Download file[%s] error !"%self.filename)
            
            #re load
            self.logger.info("Reload filename[%s] cfg[%s]",(self.filename,self.conf))
            download = DownloadHandler(self.conf, self.filename, self.source)
            TaskRun.getInstance().submit(download)
            
            self.logger.exception(e)
            
        finally:
            DownloadHandler.Threads_lock.acquire()
            try:
                DownloadHandler.dowNum -=1
            finally:
                DownloadHandler.Threads_lock.release()
                
            
