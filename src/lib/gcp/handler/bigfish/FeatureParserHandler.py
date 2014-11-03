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
        
        parser = xml.sax.make_parser()  
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        parser.setFeature(xml.sax.handler.feature_validation, 0)
        parser.setEntityResolver(BigfishEntityResolver());
        handler = BigfishDecode(self.conf,self.filename,self.source)  
        parser.setContentHandler(handler)  
        data = ""  
        with open(self.filename) as file:  
            data = file.read().strip()  
        parser.parse(StringIO.StringIO(data))  
        
        self.logger.info("Parse xml[%s] end !" % self.filename);
