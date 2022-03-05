import os

def job():
    job_txt = os.environ['TASK_SCHEDULE']+" "+ \
              os.environ['USER_NAME']+ " "+ \
              os.environ['COMMAND'] + \
              " >/proc/1/fd/1 2>/proc/1/fd/2" 
    
    job_txt += "\n\n"
    return job_txt

def create_crontab_file():
    f = open("/etc/crontab", "a")
    f.write(job())
    f.close()
    
create_crontab_file()
