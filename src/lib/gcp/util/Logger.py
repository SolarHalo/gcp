'''
Created on 2014-10-30

@author: shiwei
'''
import logging.config

    
class LoggerFactory:
    logger = None
    try:
        logging.config.fileConfig("conf/logging.conf")
        
    except Exception , e:
        logging.config.fileConfig("D:/working/workspace/pythonspace/gcp/src/conf/logging.conf")
    
    logger = logging.getLogger("example01")
    
    @staticmethod
    def getLogger():
        return LoggerFactory.logger
