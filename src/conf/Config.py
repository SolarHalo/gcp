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
    
        
    urlTemples = []
        
    for key in configs['game.bigfish'].keys():
        if key.startswith('url'):
            table = key.replace('url.','')
            urlTemple = configs['game.bigfish'][key]
            urlTemples.append([urlTemple,table])
        
    for urlTemple in urlTemples:
        cf = configs['game.bigfish']
        urls = StaticUtil.convertUrl(urlTemple, cf)
        print len(urls)
        for conf in urls:
            filepath = configs['game.bigfish']['data_path'] +StaticUtil.getPara(conf)+ StaticUtil.getTimeStrForFold() + "bigfish.xml"
            print filepath
            
except Exception as e:
    print e
