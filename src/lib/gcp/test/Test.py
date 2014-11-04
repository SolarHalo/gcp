'''
Created on 2014-11-1

@author: tiamsw
'''
import time
if __name__ == '__main__':
    var1 = "bac"
    print time.strftime('%Y-%m-%d %H:%M:%S', time.strptime("Mon, 03 Nov 2014 00:00:00 +0100"[:-6],'%a, %m %b %Y %H:%M:%S'))
          
    pass