'''
Created on Dec 1, 2011

@author: mark
'''
import datetime, time

def datetime2millis(dt=datetime.datetime.now()):
    '''
    convert python datetime to 'Java' date in milliseconds
    '''
    return int((time.mktime(dt.timetuple()) + (dt.microsecond / 1000000.)) * 1000)

def millis2datetime(millis):
    '''
    convert 'Java' date in milliseconds to python datetime
    '''
    return datetime.datetime.fromtimestamp(int(millis) // 1000)
