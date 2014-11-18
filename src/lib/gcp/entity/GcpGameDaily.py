'''
Created on 2014-11-4

@author: tiamsw
'''
import datetime
class GcpGameDaily:
    
    id = None
    gId = None
    gameId = None
    language = None
    site = None
    gametype = None
    content = None
    
    title = None
    link = None
    category = None
    pubDate = None
    description = None
    
    def __init__(self):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")