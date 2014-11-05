'''
Created on 2014-10-29

@author: tiamsw
'''


import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('./')
from conf import Config
import time

from lib.gcp.util.Logger import LoggerFactory
from lib.core.TaskRun import TaskRun
import lib.gcp.handler.bigfish.UrlParserHandler
import lib.gcp.handler.alawar.UrlParserHandler

from lib.core.TimeScheduler import TimeScheduler
from apscheduler.threadpool import ThreadPool

if __name__ == '__main__':
 
    logger = LoggerFactory.getLogger()
    
    #thread pool
    poolmin = Config.configs['sys']['threadpool.min']
    poolmax = Config.configs['sys']['threadpool.max']
    keep= Config.configs['sys']['threadpool.keep']
    pool = ThreadPool(poolmin,poolmax,keep);
    
    logger.info("Ready to start Scheduler !");
    TimeScheduler.getInstance().init(pool);
    TimeScheduler.getInstance().registerInterval(lib.gcp.handler.alawar.UrlParserHandler.UrlParserHandler(),
                                                 minutes = 17,start_date ='2014-12-02 13:17:00')
    TimeScheduler.getInstance().registerInterval(lib.gcp.handler.bigfish.UrlParserHandler.UrlParserHandler(),
                                                 minutes = 17,start_date ='2014-12-02 13:17:00')
    TimeScheduler.getInstance().start()
    logger.info("Start Scheduler end !");
    
    logger.info("Ready to start Task !");
    TaskRun.getInstance().start(treadpool= pool);
    logger.info("Start Task end!");
    
    #TaskRun.getInstance().submit(lib.gcp.handler.alawar.UrlParserHandler.UrlParserHandler())
    TaskRun.getInstance().submit(lib.gcp.handler.bigfish.UrlParserHandler.UrlParserHandler('game'))
    
    time.sleep(60*7)
    
    TaskRun.getInstance().submit(lib.gcp.handler.bigfish.UrlParserHandler.UrlParserHandler('game_catch'))
    
    TaskRun.getInstance().submit(lib.gcp.handler.bigfish.UrlParserHandler.UrlParserHandler('game_daily'))
    
    TaskRun.getInstance().submit(lib.gcp.handler.bigfish.UrlParserHandler.UrlParserHandler('game_feature'))
    
    pass
