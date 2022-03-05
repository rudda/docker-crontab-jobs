## Overview
The gol af this repository is provides a good way to create microservices
running in the schedule time by cron jobs.

## how to create a service in docker-compose

A cron job has the following definition:

    # Example of job definition:
    # |  .------------- hour (0 - 23)
    # |  |  .---------- day of month (1 - 31)
    # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
    # |  |  |  |  |
    # *  *  *  *  * user-name command to be executed

keeping it in mind, we have the following pattern <schedule-time> <user-name> <command-to-be-executed>
in order to create it, we can just to passing these args by enviroment variables as follow:

    ´´´
    environment:
        - USER_NAME=root
        - TASK_SCHEDULE=* * * * *
        - COMMAND=node --version 
    ´´´

There's a full [docker-compose sample here](docker-compose.yml)

[The entrypoint.sh file](entrypoint.sh) is responsable for call [setup.crontab.py python script](setup.crontab.py) and create
the crontab file. After crontab file is created then the cron job service is started by command 
    cron -f

### Important Notes

* env >> /etc/environment : the cron jobs not recognize the env variables so this line is very important before call cron -f
* There's a mandatory blank line in the end of crontab file

## Running by docker command line

    docker build -t <docker-custom-image-name-here> .

    docker run -it -e USER_NAME="root" -e TASK_SCHEDULE="* * * * *" -e COMMAND="node --version"  <docker-custom-image-name-here>

