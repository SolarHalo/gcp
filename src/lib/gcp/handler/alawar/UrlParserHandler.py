'''
Created on 2014-10-30

@author: tiamsw
'''
from conf import Config
from lib.gcp.util.StaticUtil import StaticUtil
from lib.gcp.handler.DownloadHandler import DownloadHandler
from lib.gcp.util.Logger import LoggerFactory
from lib.core.TaskRun import TaskRun
from lib.gcp.util.GcpConstant import GcpConstant
import os


class UrlParserHandler:
    
    logger = LoggerFactory.getLogger()

    table = None
    
    
    def __init__(self,table = None):
        self.table = table
                    
    def execute(self):
        configs = Config.getConfig()
        self.logger.info("Ready to parser url !")
        
        urlTemples = []
        
        for key in configs['game.alawar'].keys():
            if key.startswith('url'):
                attr = key.split(".")
                table = attr[1]
                locale = attr[2]
                urlTemple = configs['game.alawar'][key]
                urlTemples.append([urlTemple,table,locale])
        
        for urlTemple in urlTemples:
            if self.table is not None and urlTemple[1] != self.table:
                continue
            
            cf = configs['game.alawar']
            urls = StaticUtil.convertUrl(urlTemple, cf)
            self.logger.info("Parser xml convert count[%d]!" % len(urls));
            for conf in urls:
                filepath = os.path.join(StaticUtil.mkdir(configs['game.alawar']['data_path'], conf),
                                        StaticUtil.getTimeStrForFold() + "alawar.xml")
                #filepath = Config.configs['game.alawar']['data_path'] +StaticUtil.getPara(conf)+ StaticUtil.getTimeStrForFold() + "alawar.xml"
                download = DownloadHandler(conf, filepath, GcpConstant.Source.Alawar)
                TaskRun.getInstance().submit(download)
                
                self.logger.info("Parser xml[%s] name , url[%s] end !"%(filepath,conf));
