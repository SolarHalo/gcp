'''
Created on 2014-10-29

@author: tiamsw
'''

import ConfigDefault
from apscheduler.util import *
from lib.gcp.util.StaticUtil import StaticUtil

configs = ConfigDefault.configs

try:
    import ConfigOverride
    configs = combine_opts(ConfigOverride.configs,'',ConfigDefault.configs)
            
except Exception as e:
    print e
