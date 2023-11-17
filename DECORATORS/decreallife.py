'''
Have you ever used Decorator in real time if yes explain?
Yes! I have decorator in implementing CRON JOBS
'''

#Decorator real life example
import time
from datetime import datetime

def log_datetime_decorator(func):
    '''Log the date and time of a function'''

    def wrapper_func():
        print(f"Function:{func.__name__}")
        print(f"Run on :{datetime.today().strftime('%Y-%M-%D %H:%M:%S')}")
        print(f'{"..................."}')
        func()
    return wrapper_func

@log_datetime_decorator
def daily_cron_job():
    time.sleep(9)
    print("Daily CRON job has finished...")

@log_datetime_decorator
def weekly_cron_job():
    time.sleep(9)
    print("Weekly CRON job has finished....")

@log_datetime_decorator
def monthly_cron_job():
    time.sleep()
    print("Monthly CRON job has finished.....")

daily_cron_job()
weekly_cron_job()
monthly_cron_job()
