'''
Created on 2014-11-3

@author: tiamsw
'''
import datetime

class GcpGameCatch:
    
    
    id = None
    gId = None
    gameId = None
    language = None
    site = None
    gametype = None
    
    logoUrl = None
    imagesMed = None
    tagline = None
    offerStartDate = None 
    offerEndDate = None 
    link = None
    price = None

    timestamp = None
    
    def __init__(self):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        