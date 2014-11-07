'''
Created on 2014-10-29

@author: tiamsw
'''


from apscheduler.util import *
from lib.gcp.util.StaticUtil import StaticUtil


def getConfig():
    configs = None
    from conf import ConfigDefault
    from conf import ConfigOverride
    try:
        StaticUtil.reload_by_module_name(ConfigOverride.__name__)
        StaticUtil.reload_by_module_name(ConfigDefault.__name__)
        from conf import ConfigDefault
        from conf import ConfigOverride
        configs = combine_opts(ConfigOverride.configs,'',ConfigDefault.configs)
    except Exception as e:
        print e
    return configs