'''
Created on 2014-10-30

@author: tiamsw
'''

from apscheduler.scheduler import Scheduler

class TimeScheduler:

    instance = None
    
    def __init__(self):
        '''
        '''
    
    @staticmethod
    def getInstance():
        if TimeScheduler.instance is None:
            TimeScheduler.instance = TimeScheduler()
        return TimeScheduler.instance
    
    def init(self,threadpool = None):
        if threadpool is None :
            self.sched = Scheduler({'apscheduler.threadpool.core_threads':1,
                                    'apscheduler.threadpool.max_threads':1,
                                    'apscheduler.threadpool.keepalive':1})  
        else:
            self.sched = Scheduler({'apscheduler.threadpool':threadpool})  
        self.sched.daemonic = False 
    
    def registerCronExp(self,handler,year=None, month=None, day=None, hour=None, minute=None, second=None,
                     start_date=None):
        return self.sched.add_cron_job(handler.execute,year, month, day, None,None, 
                                       hour, minute, second,None)
        
    def registerCron(self, handler ,year=None, month=None, day=None, week=None,
                     day_of_week=None, hour=None, minute=None, second=None,
                     start_date=None):
        return self.sched.add_cron_job(handler.execute,year=None, month=None, day=None, week=None,
                     day_of_week=None, hour=None, minute=None, second=None,
                     start_date=None)

    '''
        register interval task
    '''
    def registerInterval(self, handler,weeks=0, days=0, hours=0, minutes=0,
                         seconds=0, start_date=None):
        
        return self.sched.add_interval_job(handler.execute,weeks,days,hours, minutes,
                        seconds,start_date)  
    def registerDate(self, handler,date):
        return self.sched.add_date_job(handler.execute,date)  

    def unregister(self,job):
        self.sched.unschedule_job(job)
        
    def start(self):
        self.sched.start() 