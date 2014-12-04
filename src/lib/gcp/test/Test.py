# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2014-11-1
@author: tiamsw
'''
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('./')

import time
import jieba

from lib.gcp.util.StaticUtil import StaticUtil
from conf import Config
from lib.gcp.handler.TagHandler import TagHandler

if __name__ == '__main__':
    
    tags = TagHandler()
    tags.execute()
    
    '''
    full_mode = jieba.cut("测试用例",cut_all=True)
    
    for w in full_mode:
        print w

    #print "--".join(full_mode)
    '''
    pass