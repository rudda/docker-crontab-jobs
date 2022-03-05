FROM node:17

ENV HOME=/root/
RUN apt-get update && apt-get install -y cron && which cron && \
    rm -rf /etc/cron.*/*

COPY entrypoint.sh /root/entrypoint.sh
COPY setup.crontab.py /root/setup.crontab.py
RUN chmod +x /root/entrypoint.sh

#COPY src/crontab/lifecicle /etc/crontab 

ENTRYPOINT ["/root/entrypoint.sh"]

