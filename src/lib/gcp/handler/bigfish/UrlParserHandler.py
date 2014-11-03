'''
Created on 2014-10-30

@author: tiamsw
'''
from conf import Config
from lib.gcp.handler.DownloadHandler import DownloadHandler
from lib.gcp.util.Logger import LoggerFactory
from lib.core.TaskRun import TaskRun
from lib.gcp.util.GcpConstant import GcpConstant
from lib.gcp.util.StaticUtil import StaticUtil
class UrlParserHandler:
    
    logger = LoggerFactory.getLogger()

    def __init__(self):
        '''
        '''
        
    def execute(self):
        
        self.logger.info("Ready to parser url !")

        urlTemples = []
        
        for key in Config.configs['game.bigfish'].keys():
            if key.startswith('url'):
                table = key.replace('url.','')
                urlTemple = Config.configs['game.bigfish'][key]
                urlTemples.append([urlTemple,table])
                
        for urlTemple in urlTemples:        
            cf = Config.configs['game.bigfish']
            urls = StaticUtil.convertUrl(urlTemple, cf)
            
            self.logger.info("Parser xml convert count[%d]!" % len(urls));
            for conf in urls:
                filepath = Config.configs['game.bigfish']['data_path'] +StaticUtil.getPara(conf)+ StaticUtil.getTimeStrForFold() + "bigfish.xml"
                download = DownloadHandler(conf, filepath, GcpConstant.Source.Bigfish)
                TaskRun.getInstance().submit(download)
                
                self.logger.info("Parser xml[%s] name , url[%s] end !" % (filepath, conf));