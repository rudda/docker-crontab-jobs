#!/bin/sh
env >> /etc/environment
python3 /root/setup.crontab.py 

cat /etc/crontab
#start cron in the foreground (replacing the current process)
cron -f