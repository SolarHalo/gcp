'''
Created on 2014-10-30

@author: tiamsw
'''
import time
from conf import Config
from lib.gcp.util.StaticUtil import StaticUtil
from lib.gcp.handler.DownloadHandler import DownloadHandler
from lib.gcp.util.Logger import LoggerFactory
from lib.core.TaskRun import TaskRun
from lib.gcp.util.GcpConstant import GcpConstant
class UrlParserHandler:
    
    logger = LoggerFactory.getLogger()

    def __init__(self):
        '''
        '''
                    
    def execute(self):
        self.logger.info("Ready to parser url !")
        
        urlTemples = []
        
        for key in Config.configs['game.alawar'].keys():
            if key.startswith('url'):
                table = key.replace('url.','')
                urlTemple = Config.configs['game.alawar'][key]
                urlTemples.append([urlTemple,table])
        
        for urlTemple in urlTemples:
            cf = Config.configs['game.alawar']
            urls = StaticUtil.convertUrl(urlTemple, cf)
            self.logger.info("Parser xml convert count[%d]!" % len(urls));
            for conf in urls:
                filepath = Config.configs['game.alawar']['data_path'] +StaticUtil.getPara(conf)+ StaticUtil.getTimeStrForFold() + "alawar.xml"
                download = DownloadHandler(conf, filepath, GcpConstant.Source.Alawar)
                TaskRun.getInstance().submit(download)
                
                self.logger.info("Parser xml[%s] name , url[%s] end !"%(filepath,conf));
