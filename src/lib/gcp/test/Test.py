'''
Created on 2014-11-1

@author: tiamsw
'''
import time
if __name__ == '__main__':
    var1 = "Fri, 24 Feb 2012 00:00:00 -0200"
    time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(var1[:-6],'%a, %d %b %Y %H:%M:%S'))      
    pass