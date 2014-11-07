'''
Created on 2013-8-18

@author: yuyue
'''
#  oristr like 'Saturday 11/01/2014 7:00pm' 
import os
import time
import datetime
import sys

class StaticUtil:
    
    @staticmethod
    def reload_by_module_name(module_name):  
        try:  
            module =  sys.modules[module_name]  
            reload(module)  
            __import__(module_name)  
        except KeyError:  
            print('the module is not imported')  
        except:  
            print('reload failure')  
        
    @staticmethod
    def reload_by_class(clazz):  
        try:  
            module_name = clazz.__module__  
            StaticUtil.reload_by_module_name(module_name)  
        except AttributeError:  
            print('parameter must be class or object')  


    @staticmethod
    def mkdir(fd,conf):
        new_path = fd
        
        now = datetime.datetime.now()
        new_path = os.path.join(new_path, now.strftime('%Y-%m-%d-%H'))
        if not os.path.isdir(new_path):    
            os.makedirs(new_path)
            
        new_path = os.path.join(new_path, conf['table'])
        if not os.path.isdir(new_path):    
            os.makedirs(new_path)
                    
        for key in conf.keys():
            if not key.startswith('url') and not key.startswith('table'):
                new_path = os.path.join(new_path, conf[key])
                if not os.path.isdir(new_path):    
                    os.makedirs(new_path)
        return new_path
                
        
    @staticmethod
    def getPara(conf):
        result = ''
        for key in conf.keys():
            if not key.startswith('url'):
                if type(conf[key]) is int: 
                    result += "%d"%conf[key]
                else:
                    result += "%s"%conf[key]
        return result
    
    @staticmethod
    def convertUrl(urlTemple,cf):
        datas = []
        datas.append({'url':urlTemple[0],'table':urlTemple[1]})
        varmap = {}
        prefix = "${"
        end = "}"
        for key in cf:
            if key.startswith(prefix):
                varmap[key] = cf[key]
                
        for key in varmap.keys():
            if len(datas) > 0 and datas[0]['url'].find(key) < 0:
                continue
            
            tem = []
            for data in datas:
                tem.append(data);
            datas = []
            for urlT in tem:
                
                for var in varmap[key]:
                    #copy
                    url = {}
                    for u in urlT.keys():
                        url[u] = urlT[u]
                    if type(var) is int:
                        var = "%d"%var
                    tt = url['url']
                    tt = tt.replace(key,var)
                    if tt != url['url']:
                        url['url'] = tt
                        k = key[2:-1]
                        url[k] = var 
                        datas.append(url)
        return datas
    
    @staticmethod 
    def convertDateStr(oristr): 
        us = oristr.split(" ")
        timestr = us[1]
        time = us[2]
        hour = time.split(":")[0]
        timeflag = time[len(time) - 2:]
        if(timeflag == "pm" and hour != "12"):
            hour = str(int (hour) + 12)
        timestr = timestr + " " + hour + ":" + time[len(time) - 4:len(time) - 2] + ":00"
        return timestr
    
    @staticmethod
    def getTimeStrForFold():
        return time.strftime("%Y%m%d%H%M%S", time.localtime())
    
    @staticmethod
    def getTimeStrForShow():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())   
