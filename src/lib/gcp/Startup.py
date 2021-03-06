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
from lib.gcp.util.Logger import LoggerFactory
from lib.core.TaskRun import TaskRun
import lib.gcp.handler.bigfish.UrlParserHandler
import lib.gcp.handler.alawar.UrlParserHandler
from lib.core.TimeScheduler import TimeScheduler
from apscheduler.threadpool import ThreadPool
from lib.gcp.handler.TagHandler import TagHandler
from lib.gcp.handler.GenreEnnameHandler import GenreEnnameHandler

if __name__ == '__main__':
 
    logger = LoggerFactory.getLogger()
    
    #thread pool
    configs = Config.getConfig()
    poolmin = configs['sys']['threadpool.min']
    poolmax = configs['sys']['threadpool.max']
    keep = configs['sys']['threadpool.keep']
    pool = ThreadPool(poolmin,poolmax,keep);
    
    logger.info("Ready to start Task !");
    TaskRun.getInstance().start(treadpool= pool);
    logger.info("Start Task end!");
    
    logger.info("Ready to start Scheduler !");
    TimeScheduler.getInstance().init(pool);
    TimeScheduler.getInstance().registerInterval(lib.gcp.handler.alawar.UrlParserHandler.UrlParserHandler(),
                                                 days = 1,start_date ='2014-11-02 00:00:00')
    
    TimeScheduler.getInstance().registerInterval(lib.gcp.handler.bigfish.UrlParserHandler.UrlParserHandler('game'),
                                                 days = 1,start_date ='2014-11-02 00:00:00')
    
    TimeScheduler.getInstance().registerInterval(lib.gcp.handler.bigfish.UrlParserHandler.UrlParserHandler('game_catch'),
                                                 days = 1,start_date ='2014-11-02 01:00:00')
    
    TimeScheduler.getInstance().registerInterval(lib.gcp.handler.bigfish.UrlParserHandler.UrlParserHandler('game_daily'),
                                                 days = 1,start_date ='2014-11-02 01:00:00')
    
    TimeScheduler.getInstance().registerInterval(lib.gcp.handler.bigfish.UrlParserHandler.UrlParserHandler('game_feature'),
                                                 days = 1,start_date ='2014-11-02 01:00:00')
    
    TimeScheduler.getInstance().registerInterval(TagHandler(),days = 1,start_date ='2014-11-02 02:00:00');
    
    TimeScheduler.getInstance().registerInterval(GenreEnnameHandler(),days = 1,start_date ='2014-11-02 02:00:00');
    
    TimeScheduler.getInstance().start()
    logger.info("Start Scheduler end !");
    
    pass
