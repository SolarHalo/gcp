'''
Created on 2014-10-29

@author: tiamsw
'''

import ConfigDefault
import ConfigOverride
from apscheduler.util import *
from lib.gcp.util.StaticUtil import StaticUtil

configs = ConfigDefault.configs

try:
    
    StaticUtil.reload_by_module_name(ConfigOverride.__name__)
    StaticUtil.reload_by_module_name(ConfigDefault.__name__)
    import ConfigOverride
    import ConfigDefault
    configs = combine_opts(ConfigOverride.configs,'',ConfigDefault.configs)
            
except Exception as e:
    print e
