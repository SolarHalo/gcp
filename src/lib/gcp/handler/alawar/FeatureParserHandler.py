'''
Created on 2014-10-30

@author: tiamsw
'''

import xml.sax
import StringIO
from lib.gcp.handler.alawar.AlawarDecode import AlawarDecode
from lib.gcp.handler.alawar.AlawarDecode import AlawarEntityResolver
from lib.gcp.util.Logger import LoggerFactory

class FeatureParserHandler:

    logger = LoggerFactory.getLogger()

    source = None
    
    filename = None
    
    conf = None
    
    def __init__(self, filename, source,conf):
        self.filename = filename
        self.source = source
        self.conf = conf
    
    def execute(self):
        self.logger.info("Ready to parse xml[%s] !" % self.filename)
        
        try:
            
            parser = xml.sax.make_parser()  
            parser.setFeature(xml.sax.handler.feature_namespaces, 0)
            parser.setFeature(xml.sax.handler.feature_validation, 0)
            parser.setEntityResolver(AlawarEntityResolver())
            handler = AlawarDecode(self.conf,self.filename,self.source)  
            parser.setContentHandler(handler)  
            data = ""  
            with open(self.filename) as xmlfile:  
                data = xmlfile.read().strip()  
            parser.parse(StringIO.StringIO(data))
        except Exception , e:
            self.logger.error("Parse Xml[%s] %s error !"%(self.filename,self.source))
            self.logger.exception(e)  
        
        self.logger.info("Parse xml[%s] end !" % self.filename)
        
