import os

def head():
    head_txt = """SHELL=/bin/bash
BASH_ENV=/etc/environment

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed" 

"""
    return head_txt

def job():
    job_txt = os.environ['TASK_SCHEDULE']+" "+ os.environ['USER_NAME']+ " "+ os.environ['COMMAND'] + " >/proc/1/fd/1 2>/proc/1/fd/2" 
    job_txt += "\n\n"
    return job_txt

def create_crontab_file():
    #os.remove("/etc/crontab")
    f = open("/etc/crontab", "a")
    #f.write(head())
    f.write(job())
    f.close()


create_crontab_file()
