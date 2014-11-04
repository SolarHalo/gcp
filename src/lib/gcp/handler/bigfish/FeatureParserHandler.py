'''
Created on 2014-10-29

@author: tiamsw
@note: bigfish parse

'''
import xml.sax
import StringIO
from lib.gcp.handler.bigfish.BigfishDecode import BigfishDecode
from lib.gcp.handler.bigfish.BigfishDecode import BigfishEntityResolver
from lib.gcp.util.Logger import LoggerFactory
from lib.gcp.handler.bigfish.CatchDecode import CatchDecode
from lib.gcp.handler.bigfish.DailyDecode import DailyDecode
from lib.gcp.handler.bigfish.FeatureDecode import FeatureDecode
        
class FeatureParserHandler:
    
    logger = LoggerFactory.getLogger()
    
    filename = None
    
    source = None
    
    conf = None
    
    def __init__(self, filename, source,conf):
        self.filename = filename
        self.source = source
        self.conf = conf
        
    def execute(self):
        self.logger.info("Ready to parse xml[%s] , %s !" % (self.filename,self.source));
        
        try:
            handler = None 
            if self.conf['table'] == 'game_catch':
                handler = CatchDecode(self.conf,self.filename,self.source)
            elif self.conf['table'] == 'game':
                handler = BigfishDecode(self.conf,self.filename,self.source)
            elif self.conf['table'] == 'game_daily':
                #handler = DailyDecode(self.conf,self.filename,self.source)
                self.logger.info("Parse Xml[%s] %s decode not implement !" % (self.filename,self.source))
                return 
            elif self.conf['table'] == 'game_feature':
                handler = FeatureDecode(self.conf,self.filename,self.source)
    
            parser = xml.sax.make_parser()  
            parser.setFeature(xml.sax.handler.feature_namespaces, 0)
            parser.setFeature(xml.sax.handler.feature_validation, 0)
            parser.setEntityResolver(BigfishEntityResolver());
            
            parser.setContentHandler(handler)  
            data = ""  
            with open(self.filename) as filexml:  
                data = filexml.read().strip()  
            parser.parse(StringIO.StringIO(data))  
        except Exception , e:
            self.logger.error("Parse Xml[%s] %s error !"%(self.filename,self.source))
            self.logger.exception(e)
            #failed redownload
             
            
            
        self.logger.info("Parse xml[%s] end !" % self.filename);
