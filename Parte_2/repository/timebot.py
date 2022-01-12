import os
from datetime import datetime, timedelta
from time import sleep

def the_time():
    time_execute = datetime.now()
    time_execute = time_execute.replace(
        day=time_execute.day,
        hour= time_execute.hour,
        minute=time_execute.minute,
        second=time_execute.second,
        microsecond = 0
    )
    return time_execute

