'''
Created on 2014-11-1

@author: tiamsw
'''
import time
from lib.gcp.util.StaticUtil import StaticUtil
from conf import Config
import sys
if __name__ == '__main__':
    configs = Config.getConfig()
    print configs['sys']['db.batch.size']
    pass