'''
Created on 2014-10-30

@author: shiwei
'''
import Queue  
import threading  
from lib.gcp.util.Logger import LoggerFactory

class TaskRun(object):
    
    logger = LoggerFactory.getLogger()
 
    work_queue = None
    
    threads = None
    
    instance = None
    
    treadpool = None
    
    @staticmethod
    def getInstance():
        if TaskRun.instance is None:
            TaskRun.instance = TaskRun()
        return TaskRun.instance
    
    def __init__(self):
        '''
        '''
    def start(self, qLen=0, tpLen=0,treadpool=None):
        self.treadpool = treadpool
        if self.treadpool is None:
            self.threads = []
            self.work_queue = Queue.Queue(qLen)  
            for i in range(0, tpLen):
                tp = threading.Thread(target=self.svc)
                self.threads.append(tp)
                tp.setName('pool-thread-%d' % i)
                tp.start()
                self.logger.info("Start thread[%s] end !" % tp.getName());

    def submit(self, handler):
        if self.treadpool is None:
            self.work_queue.put(handler)
        else:
            self.treadpool.submit(handler.execute)
        
    def svc(self):
        while True:
            try:
                handler = self.work_queue.get()
                if handler is not None:
                    handler.execute()
            except Exception , e:
                self.logger.error(e)
                
