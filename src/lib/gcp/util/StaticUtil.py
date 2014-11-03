'''
Created on 2013-8-18

@author: yuyue
'''
#  oristr like 'Saturday 11/01/2014 7:00pm' 
import time
class StaticUtil:
    
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
