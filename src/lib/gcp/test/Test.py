'''
Created on 2014-11-1

@author: tiamsw
'''
import time
from lib.gcp.util.StaticUtil import StaticUtil
from conf import Config
import sys
if __name__ == '__main__':
    while True:
        StaticUtil.reload_by_module_name(Config.__name__)
        from conf import Config
        time.sleep(5)
    pass