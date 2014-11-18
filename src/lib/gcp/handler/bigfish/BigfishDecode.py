
'''
Created on 2014-10-30

@author: shiwei
'''
from xml.sax import ContentHandler
from lib.gcp.entity.GcpGame import GcpGame
from lib.gcp.util.Logger import LoggerFactory
import xml.sax
from conf import Config
from lib.gcp.handler.DaoHandler import DaoHandler
from lib.core.TaskRun import TaskRun
import time

class BigfishEntityResolver(xml.sax.handler.EntityResolver):
    def resolveEntity(self, publicId, systemId):
        configs = Config.getConfig()
        return configs['game.bigfish']['dtd'][0] + systemId
    

class BigfishDecode(ContentHandler):  
    
    logger = LoggerFactory.getLogger()
    
    sitePrix = None
    assets = None
    
    batchSize = 100
    
    baseBuffer = None
    
    counter = 0
    
    buffer = ''
    
    entity = None
    
    conf = None
    filename = None
    source = None
    def __init__(self,conf,filename,source):
        self.conf = conf
        self.filename = filename
        self.source = source
        
        configs = Config.getConfig()
        self.batchSize = configs['sys']['db.batch.size']
        self.sitePrix = configs['game.bigfish']['dtd'][1]
        self.assets =  configs['game.bigfish']['dtd'][2]

    def startDocument(self):
        self.buffer = ''
        self.baseBuffer = []
        self.logger.info("Decode file[%s] source[%s] !"%(self.filename,self.source))
        
    def endDocument(self):  
        self.logger.info( 'game===counter:%d' % self.counter);
        if len(self.baseBuffer) > 0:
            dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
            TaskRun.getInstance().submit(dao)
    def startElement(self, name, attrs):
        self.buffer = ''
        if 'game' == name:
            self.entity = GcpGame()
            self.entity.gametype = self.conf['gametype']
            self.entity.language = self.conf['locale']
            self.counter = self.counter + 1
        elif name == 'genreid':
            self.entity.genreName = attrs['name']
            
            
    def endElement(self, name):
        if self.entity is None:
            return   
        if name == 'gameid':
            self.entity.gameId = self.buffer
        elif name == 'gamename':
            self.entity.gameName = self.buffer
        elif name == 'family':
            self.entity.family = self.buffer
        elif name == 'shortdesc':
            self.entity.shortdesc = self.buffer
        elif name == 'meddesc':
            self.entity.meddesc = self.buffer
        elif name == 'longdesc':
            self.entity.longdesc = self.buffer
        elif name == 'bullet1':
            self.entity.bullet1 = self.buffer
        elif name == 'bullet2':
            self.entity.bullet2 = self.buffer
        elif name == 'bullet3':
            self.entity.bullet3 = self.buffer
        elif name == 'bullet4':
            self.entity.bullet4 = self.buffer
        elif name == 'bullet5':
            self.entity.bullet5 = self.buffer
        elif name == 'foldername':
            self.entity.foldername = self.buffer
        elif name == 'price':
            self.entity.price = self.buffer
        elif name == 'gamesize':
            self.entity.gamesize = self.buffer
        elif name == 'gamerank':
            self.entity.gamerank = self.buffer
        elif name == 'hasvideo':
            self.entity.video = self.buffer
        elif name == 'hasflash':
            self.entity.flash = self.buffer
        elif name == 'hasdwfeature':
            self.entity.imgDwFeature = self.buffer
            self.entity.flashDwFeature = self.buffer
        elif name == 'dwwidth':
            self.entity.dwwidth = self.buffer
        elif name == 'dwheight':
            self.entity.dwheight = self.buffer
        elif name == 'releasedate' and self.buffer is not None and self.buffer != '':
            try:
                self.entity.releasedate = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(self.buffer,'%Y-%m-%d %H:%M:%S'))
            except Exception , e:
                self.logger.error("releasedate error %s , %s!"%(self.buf,self.source))
                self.logger.error(e);
        elif name == 'sysreqos':
            self.entity.systemreq = 'OS: ' + self.buffer 
        elif name == 'sysreqmhz':
            self.entity.systemreq = self.entity.systemreq + ' / CPU: ' + self.buffer 
        elif name == 'sysreqmem':
            self.entity.systemreq = self.entity.systemreq + ' / RAM: ' + self.buffer
        elif name == 'sysreqdx':
            self.entity.systemreq = self.entity.systemreq + ' / DirectX: ' + self.buffer
        elif name == 'sysreqhd':
            self.entity.systemreq = self.entity.systemreq + ' / ' + self.buffer
            
        elif 'game' == name:
            #  url
            assetname = self.entity.foldername ;
            if assetname is not None:
                assetname = assetname.replace(self.entity.language+"_", "")
                
            if self.entity.gametype == 'pc':
                self.entity.downloadurl     = self.sitePrix +'.'+self.entity.language + "/download-games/" + self.entity.gameId + "/" + assetname +"/download.html?channel=affiliates&identifier={afcode}"
                self.entity.downloadiframe  = self.sitePrix +'.'+self.entity.language + "/download-games/" + self.entity.gameId + "/" + assetname+"/download_pnp.html?channel=affiliates&identifier={afcode}"
                
                self.entity.buyurl      = self.sitePrix +'.'+self.entity.language+"/download-games/"+ self.entity.gameId+"/"+assetname+"/buy.html?channel=affiliates&identifier={afcode}"
                self.entity.buyiframe   = self.sitePrix +'.'+self.entity.language+"/download-games/"+ self.entity.gameId+"/"+assetname+"/buy_pnp.html?channel=affiliates&identifier={afcode}"
                
            elif self.entity.gametype == 'mac':
                self.entity.downloadurl     = self.sitePrix +'.'+self.entity.language+"/download-games/mac/"+self.entity.gameId+assetname+"/"+ "/download.html?channel=affiliates&identifier={afcode}"
                self.entity.downloadiframe  = self.sitePrix +'.'+self.entity.language+"/download-games/mac/"+self.entity.gameId+assetname+"/"+ "/download_pnp.html?channel=affiliates&identifier={afcode}"
                
                self.entity.buyurl      = self.sitePrix +'.'+self.entity.language+"/download-games/mac/"+ self.entity.gameId+"/"+assetname+"/buy.html?channel=affiliates&identifier={afcode}"
                self.entity.buyiframe   = self.sitePrix +'.'+self.entity.language+"/download-games/mac/"+ self.entity.gameId+"/"+assetname+"/buy_pnp.html?channel=affiliates&identifier={afcode}"
            else:
                self.entity.downloadurl     = self.sitePrix +'.'+self.entity.language+"/online-games/"+self.entity.gameId+"/"+ assetname+"/index.html?channel=affiliates&identifier={afcode}"
                self.entity.downloadiframe  = self.sitePrix +'.'+self.entity.language+"/online-games/"+self.entity.gameId+"/"+ assetname+"/index_pnp.html?channel=affiliates&identifier={afcode}"
            #movie
            if self.entity.video == 'yes':
                self.entity.video = self.assets +"/"+ self.entity.foldername+"/"+assetname+".flv"
            else:
                self.entity.video = None;
            #video
            if self.entity.flash == 'yes':
                self.entity.flash = self.assets +"/"+ self.entity.foldername+"/"+assetname+"_175x150.swf"
            else:
                self.entity.flash = None
            
            #img
            self.entity.imgSmall        = self.assets +"/"+self.entity.foldername + "/" + assetname+"_60x40.jpg"
            self.entity.imgMed          = self.assets +"/"+self.entity.foldername + "/" + assetname+"_80x80.jpg"
            self.entity.imgFeature      = self.assets +"/"+self.entity.foldername + "/" + assetname+"_feature.jpg"
            self.entity.imgSubfeature   = self.assets +"/"+self.entity.foldername + "/" + assetname+"_subfeature.jpg"
            
            self.entity.imgThumb1   = self.assets +"/"+self.entity.foldername + "/th_screen1.jpg" 
            self.entity.imgThumb2   = self.assets +"/"+self.entity.foldername + "/th_screen2.jpg" 
            self.entity.imgThumb3   = self.assets +"/"+self.entity.foldername + "/th_screen3.jpg" 
            
            self.entity.imgScreen1  = self.assets +"/"+self.entity.foldername + "/screen1.jpg" 
            self.entity.imgScreen2  = self.assets +"/"+self.entity.foldername + "/screen2.jpg" 
            self.entity.imgScreen3  = self.assets +"/"+self.entity.foldername + "/screen3.jpg" 
            
            if self.entity.imgDwFeature == 'yes':
                self.entity.imgDwFeature = self.assets +"/"+self.entity.foldername + "/" + assetname+"_"+self.entity.dwwidth+"x"+self.entity.dwheight+".jpg"
            else:
                self.entity.imgDwFeature = None
                
            if self.entity.flashDwFeature == 'yes':
                self.entity.flashDwFeature = self.assets +"/"+self.entity.foldername + "/" + assetname+"_"+self.entity.dwwidth+"x"+self.entity.dwheight+".swf"
            else:
                self.entity.flashDwFeature = None  
              
            self.baseBuffer.append(self.entity)
            if len(self.baseBuffer) >= BigfishDecode.batchSize:
                dao = DaoHandler(self.filename,self.conf,self.baseBuffer,self.source)
                TaskRun.getInstance().submit(dao)
                self.baseBuffer = []
            self.entity = None
                
    def characters(self, content):  
        self.buffer += content
