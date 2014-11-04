'''
Created on 2014-10-30

@author: shiwei
'''
import logging.config

    
class LoggerFactory:
    logger = None
    try:
        logging.config.fileConfig("conf/logger.conf")
        
    except Exception , e:
        logging.config.fileConfig("D:/working/workspace/pythonspace/gcp/src/conf/logger.conf")
    
    logger = logging.getLogger("example")
    
    @staticmethod
    def getLogger():
        return LoggerFactory.logger
