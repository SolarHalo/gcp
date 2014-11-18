'''
Created on 2014-11-3

@author: tiamsw
'''
import datetime
class GcpGameFeature:

    id = None
    gId = None
    gameId = None
    language = None
    site = None
    gametype = None
    
    hasdwfeature = None 
    dwwidth = None 
    dwheight = None 
    gamerank = None 
    releasedate = None
    
    def __init__(self):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")   