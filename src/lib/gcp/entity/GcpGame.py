'''
Created on 2014-10-30

@author: shiwei
'''

class GcpGame:
    
    gameId = None
    gameName = None
    family = None
    genreName = None
    shortdesc = None
    
    meddesc = None
    longdesc = None
    price = None
    gamerank = None
    releasedate = None
    
    gamesize = None
    language = None
    site = None
    gametype = None
    systemreq = None
    
    bullet1 = None
    bullet2 = None
    bullet3 = None
    bullet4 = None
    bullet5 = None
    
    imgSmall = None
    imgMed = None
    imgSubfeature = None
    imgFeature = None
    
    imgThumb1 = None
    imgThumb2 = None
    imgThumb3 = None
    
    imgScreen1 = None
    imgScreen2 = None
    imgScreen3 = None
    
    video = None
    flash = None
    downloadurl = None
    buyurl = None
    downloadiframe = None
    buyiframe = None
    
    foldername = None
    
    def __init__(self):
        '''
        '''

    def toString(self):
        return 'gameId:%s, gameName:%s, family:%s, familyid:%s, \
        productid:%s, genreid:%s, genreName:%s, allgenreid:%s' % \
        (self.gameId, self.gameName, self.family, self.familyid,
         self.productid, self.genreid, self.genreName, self.allgenreid)
